# CSV preparation validation

Trial: October 23, 2026. Input: existing Treez and METRC workbook. Period: October 1, 2025–September 30, 2026. Original workbook was not modified. This validates preparation, not reconciliation or API completeness.

| Population | Nonblank input rows | Output rows |
| --- | ---: | ---: |
| Treez Medical | 53,789 | 53,789 |
| Treez Adult Use | 196,607 | 196,607 |
| Treez Non-METRC | 6,164 | 6,164 |
| METRC Medical | 49,090 | 49,090 |
| METRC Adult Use | 181,671 | 181,671 |

Independent CSV readback confirmed counts for every population. All nonblank source rows were retained for this reporting window. No repeated ticket-line IDs were observed in the medical/adult Treez populations. Distinct transactions were not deduplicated.

All preparation issues arose in Non-METRC: 99 invalid/blank amounts, 57 missing/invalid dates, 49 missing line IDs, and six repeated line-ID occurrences. Some issue types occur on the same row. These are preparation issues, not established transaction errors. Examples include rows with blank transaction identifiers and dates and some rows with blank Net Sales. They require review before using that population as clean transaction data. No records were deleted to make controls agree.

All five populations show activity on 364 dates, with no activity on December 25, 2025. This may represent a store closure; it is not proof of a missing export or complete coverage. Confirm against operating/report records.

Two automated tests passed: retention of distinct same-time/tag sales and exact decimal text, no overwrite of existing run directories, and explicit failure when required populations are absent. Workbook processing completed successfully with issues reported separately. Windows launcher was created but cannot be executed on this Linux host; local Windows/Python validation remains pending.

No transaction pairing, unit conversion, correction recommendation or full source-total reconciliation has been performed by this utility. No raw records, identifiers or production extracts are committed to Git. The prepared data package is supplied separately for review.
