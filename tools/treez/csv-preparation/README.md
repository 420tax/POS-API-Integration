# Treez and METRC CSV preparation pilot

This utility prepares existing exports for Power Query. It does not download from Treez, match transactions, determine corrections, or replace the existing reconciliation. Original files are read only. Output retains each source row and records source population/row for tracing. No customer/patient identifiers, addresses, employee names or free-text notes are exported.

## Requirements

Python 3.10 or newer. CSV mode uses only Python's standard library. XLSX mode additionally requires openpyxl configured by technical support. Staff do not edit Python code. No API credentials are required.

## Run on Windows

From this directory, use:

```powershell
py prepare_exports.py --workbook "C:\ClientData\Treez and METRC Data.xlsx" --output "C:\ClientData\prepared\run-001" --start 2025-10-01 --end 2026-09-30
```

Use a new output directory for every run. The program refuses to overwrite an existing directory. A large workbook may take several minutes; one progress line appears per source population. If an error occurs, do not refresh Power Query against that run.

For CSV mode, place files named after source populations in one input folder:

- Treez_PC_000398.csv
- Treez_AU_R_000343.csv
- METRC Med.csv
- METRC AU.csv
- Treez_Non_METRC.csv (optional)

```powershell
py prepare_exports.py --csv-folder "C:\ClientData\exports" --output "C:\ClientData\prepared\run-002" --start 2025-10-01 --end 2026-09-30
```

CSV inputs must use the existing workbook's exact headers. This version accepts one already-combined file per population, not twelve raw monthly downloads. Monthly append/coverage configuration needs the original download layout. UTF-8 CSV is supported; date formats are ISO or US month/day/year. Unsupported dates appear in preparation issues, rather than being guessed. Source numbers must use plain decimal notation without currency symbols/thousands separators; invalid amounts are flagged.

## Review output

Read manifest.json and preparation_issues.csv first. PREPARED means the preparation ran, not that reconciliation is complete. PREPARED_WITH_ISSUES requires review. FAILED is not usable.

Medical, adult-use and non-METRC records remain separate. Totals are unrounded sums of the exported monetary fields. No sales are deduplicated or matched. Repeat ticket-line IDs are flagged but retained. Out-of-period rows are logged and excluded. Invalid/missing dates remain in detail and are flagged. Missing amounts are not converted to zero. Missing transaction dates do not establish gaps in export coverage, and observed min/max dates do not establish completeness.

Workbook numbers are read as stored, including Excel floating-point representations. They cannot recover the original CSV decimal text. Timezone offsets are not invented. METRC Price is line-level; Total Price is intentionally omitted to avoid summing receipt totals repeatedly.

Power Query can import each CSV using Data > Get Data > From Text/CSV. Explicitly set identifiers/tags/licenses to Text and numeric columns to appropriate numeric types. These outputs are a staging layer, not new reconciliation queries. Keep the last accepted output until a new run is reviewed.

All live source/output files stay outside Git. Only reusable code, tests and nonconfidential validation notes belong here.

## Validation

```powershell
py -m unittest discover -s tests
```

Tests cover decimal preservation and retention of distinct same-time/tag rows, refusal to overwrite runs, and explicit failure for missing populations. See validation.md for the actual workbook trial. No live API call has been made.
