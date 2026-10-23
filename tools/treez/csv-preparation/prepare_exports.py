"""Prepare Treez/METRC exports without changing or matching source records."""
import argparse
import csv
import hashlib
import json
import os
from collections import Counter
from datetime import date, datetime, time, timedelta
from decimal import Decimal, InvalidOperation
from pathlib import Path

TREEZ = ['Date Open','Time Opened','Date Last Modified','Time Last Modified','Date Closed','Time Closed','Ticket ID','Ticket Line ID','Ticket Type','Type','Product Type','Subtype','State Tracking ID','Receiving License','Qty','Total Weight','Amount','Unit of Measure','Gross Sales','Discounts','Returns','Net Sales','Taxes','Gross Receipts','Inventory Type']
METRC = ['Sales Document No.','Sales Date/Time','Label','Category','Quantity Sold','UoM','Price','Unit Vol.','Unit Vol. UoM','Unit Wgt.','Unit Wgt. UoM']
SHEETS = {'Treez_PC_000398': ('treez_medical', TREEZ, 'Date Closed', 'Net Sales'), 'Treez_AU_R_000343': ('treez_adult', TREEZ, 'Date Closed', 'Net Sales'), 'Treez_Non_METRC': ('treez_non_metrc', TREEZ, 'Date Closed', 'Net Sales'), 'METRC Med': ('metrc_medical', METRC, 'Sales Date/Time', 'Price'), 'METRC AU': ('metrc_adult', METRC, 'Sales Date/Time', 'Price')}

def serial(v):
    if v is None: return ''
    if isinstance(v, (datetime, date, time)): return v.isoformat()
    return str(v)

def day(v):
    if isinstance(v, datetime): return v.date()
    if isinstance(v, date): return v
    s = str(v or '').strip()
    if not s: return None
    for fmt in ('%Y-%m-%d','%m/%d/%Y','%m/%d/%y'):
        try: return datetime.strptime(s.split('T')[0].split(' ')[0], fmt).date()
        except ValueError: pass
    raise ValueError('Unsupported date format')

def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda:f.read(1024*1024), b''): h.update(b)
    return h.hexdigest()

def prepare(sources, output, start, end):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=False)
    manifest = {'status':'INCOMPLETE','period_start':str(start),'period_end':str(end),'tables':{},'limitations':['Preparation only: no transaction matching or corrections.','Observed transaction dates do not prove export coverage.','Workbook floating-point values are preserved as stored; original CSV decimal text may differ.','No timezone is assigned to naive source timestamps.']}
    issues = []
    try:
        for source_name, headers, rows in sources:
            if source_name not in SHEETS: continue
            name, fields, date_field, money_field = SHEETS[source_name]
            if name in manifest['tables']: raise ValueError('Duplicate source population: '+name)
            if len(headers) != len(set(headers)): raise ValueError('Duplicate column headers: '+source_name)
            missing = set(fields) - set(headers)
            if missing: raise ValueError('Missing columns in '+source_name+': '+', '.join(sorted(missing)))
            indices = {k:headers.index(k) for k in fields}
            count = kept = 0
            total = Decimal(0)
            dates, keys, types, licenses = Counter(), Counter(), Counter(), Counter()
            path = output/(name+'.csv')
            with path.open('w',newline='',encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['Source Population','Source Row']+fields)
                for n, row in enumerate(rows, 2):
                    if not any(v is not None and v != '' for v in row): continue
                    count += 1
                    data = {k: row[i] if i<len(row) else None for k,i in indices.items()}
                    try: dt = day(data[date_field])
                    except ValueError: dt = None
                    if dt is None:
                        issues.append([name,n,'MISSING_OR_INVALID_DATE'])
                    elif not start <= dt <= end:
                        issues.append([name,n,'OUT_OF_PERIOD'])
                        continue
                    writer.writerow([source_name,n]+[serial(data[k]) for k in fields])
                    kept += 1
                    if dt: dates[str(dt)] += 1
                    try:
                        amount = Decimal(str(data[money_field]))
                        if not amount.is_finite(): raise InvalidOperation
                        total += amount
                    except (InvalidOperation, ValueError): issues.append([name,n,'INVALID_AMOUNT'])
                    if name.startswith('treez'):
                        key = str(data['Ticket Line ID'] or '')
                        if not key: issues.append([name,n,'MISSING_LINE_ID'])
                        else: keys[key] += 1
                        types[str(data['Type'])] += 1
                        licenses[str(data['Receiving License'])] += 1
                        if name != 'treez_non_metrc' and not data['State Tracking ID']: issues.append([name,n,'MISSING_TAG'])
                    elif not data['Label']: issues.append([name,n,'MISSING_TAG'])
            duplicate_count = sum(v-1 for v in keys.values())
            if duplicate_count: issues.append([name,'','REPEATED_LINE_IDS:'+str(duplicate_count)])
            manifest['tables'][name] = {'source_rows':count,'output_rows':kept,'amount_total':str(total),'observed_date_min':min(dates,default=None),'observed_date_max':max(dates,default=None),'dates_with_activity':len(dates),'daily_rows':dict(sorted(dates.items())),'repeated_line_id_rows':duplicate_count,'transaction_types':dict(types),'receiving_licenses':dict(licenses),'sha256':sha(path)}
            print(name+': '+str(kept)+' rows',flush=True)
        required = {'treez_medical','treez_adult','metrc_medical','metrc_adult'}
        if required-set(manifest['tables']): raise ValueError('Missing required source populations')
        with (output/'preparation_issues.csv').open('w',newline='',encoding='utf-8-sig') as f:
            w=csv.writer(f);w.writerow(['Population','Source Row','Issue']);w.writerows(issues)
        manifest['issue_count']=len(issues)
        manifest['status']='PREPARED_WITH_ISSUES' if issues else 'PREPARED'
    except Exception:
        manifest['status']='FAILED'
        raise
    finally:
        (output/'manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    return manifest

def workbook_sources(path):
    try: import openpyxl
    except ImportError: raise SystemExit('Workbook input requires openpyxl. Use CSV input or ask your technical support to configure the environment.')
    wb=openpyxl.load_workbook(path,read_only=True,data_only=True)
    try:
        for s in wb:
            if s.title in SHEETS:
                rows=s.iter_rows(values_only=True)
                yield s.title,list(next(rows)),rows
    finally: wb.close()

def csv_sources(folder):
    for name in SHEETS:
        p=Path(folder)/(name+'.csv')
        if p.exists():
            with p.open(newline='',encoding='utf-8-sig') as f:
                rows=csv.reader(f)
                yield name,next(rows),rows

def main():
    p=argparse.ArgumentParser(description=__doc__)
    source=p.add_mutually_exclusive_group(required=True)
    source.add_argument('--workbook');source.add_argument('--csv-folder')
    p.add_argument('--output',required=True);p.add_argument('--start',required=True,type=date.fromisoformat);p.add_argument('--end',required=True,type=date.fromisoformat)
    a=p.parse_args()
    if a.end<a.start: p.error('End date precedes start date')
    sources=workbook_sources(a.workbook) if a.workbook else csv_sources(a.csv_folder)
    m=prepare(sources,a.output,a.start,a.end)
    print(m['status']+'. Review manifest.json and preparation_issues.csv before Power Query use.')

if __name__=='__main__': main()
