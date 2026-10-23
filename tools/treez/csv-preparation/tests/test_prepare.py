import csv
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from prepare_exports import prepare, SHEETS

class PreparationTests(unittest.TestCase):
    def sources(self):
        for title,(name,fields,dt,money) in SHEETS.items():
            if name=='treez_non_metrc': continue
            records=[]
            for idx in range(2):
                d={k:'' for k in fields};d[dt]='2026-01-01';d[money]='0.100000000001'
                if name.startswith('treez'):
                    d.update({'Ticket ID':str(idx),'Ticket Line ID':str(idx),'State Tracking ID':'SAME-TAG','Time Closed':'10:00:00'})
                else: d.update({'Sales Document No.':str(idx),'Label':'SAME-TAG'})
                records.append([d[k] for k in fields])
            yield title,fields,records

    def test_distinct_sales_and_precision(self):
        with tempfile.TemporaryDirectory() as t:
            out=Path(t)/'run'
            m=prepare(self.sources(),out,date(2026,1,1),date(2026,1,31))
            self.assertEqual(m['tables']['treez_medical']['output_rows'],2)
            self.assertEqual(m['tables']['treez_medical']['amount_total'],'0.200000000002')
            self.assertNotIn('Customer Name',(out/'treez_medical.csv').read_text())
            with self.assertRaises(FileExistsError): prepare(self.sources(),out,date(2026,1,1),date(2026,1,31))

    def test_missing_population_fails(self):
        with tempfile.TemporaryDirectory() as t:
            out=Path(t)/'run'
            with self.assertRaises(ValueError): prepare([],out,date(2026,1,1),date(2026,1,31))
            self.assertIn('FAILED',(out/'manifest.json').read_text())

if __name__=='__main__': unittest.main()
