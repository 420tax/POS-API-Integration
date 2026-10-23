# Dutchie Extraction and Daily Sales Posting — Draft Pilot Specification

Prepared October 23, 2026. Proposed behavior; not implemented or vendor-certified.

## Scope

Read authorized Dutchie POS data for accounting/METRC reconciliation and up to 12 months of history. Prepare reviewed daily journal entries and develop QBO submission separately. Keep manual CSV intake and SaaSant available during validation.

## Staff workflow

1. Select approved client, location and date range.
2. Extract or import source data.
3. Review counts, coverage, control totals and exceptions.
4. Review proposed daily entries.
5. Submit explicitly approved entries through the future QBO connection.
6. Review posting confirmations and exceptions.

Staff should not edit Python or manually manipulate JSON during routine operation.

## Proposed tables

| Table | Intended contents / controls |
| --- | --- |
| Extraction manifest | Source, location, request windows, extraction time, counts, errors, schema version and completeness status |
| Transactions | Stable source identity, dates, status, gross/discount/net/tax/fees/rounding, return references |
| Sales lines | Parent key, original line reference, tag/license attribution, quantity/unit and original precision |
| Taxes / discounts / payments | Separate child records keyed to source parents; no one-to-many revenue multiplication |
| Register activity | Separate cash movements and adjustments; avoid counting cash drops/closeouts as sales |
| Daily controls | Reconciliation to Closing Report, tender/settlement controls and METRC where applicable |
| JE preview | Date, entry identity, accounts, debit/credit, description, dimensions and source references |
| Posting register | QBO company, source period/entry identity, payload fingerprint, review status, attempt state, returned transaction ID and verified totals |

These are target requirements. Vendor-confirmed fields and live tests must establish mappings; do not fill missing source facts by assumption.

## Acceptance

- Complete date/location/license coverage, with missing/failed windows distinguished from no activity.
- Preserve distinct sales sharing a timestamp/tag; no arbitrary deduplication or pairing.
- Stable identities survive repeat extraction; use documented corrections rather than duplicate accumulation.
- Full/partial returns, voids, later edits, package splits, weighted units, mixed tenders and daylight-saving boundaries tested.
- Decimal-safe parsing; explicit rounding bridge to control reports.
- Every JE balances and reconciles to reviewed accounting rules.
- Existing QBO/SaaSant postings identified before any write.
- Partial failures and uncertain writes resolved through lookup/reconciliation before retry.
- Test QBO sandbox first, then a separately authorized small production run.
- Keep returned QBO IDs and read-back evidence.
- Measure actual staff time and errors against the current SaaSant workflow; do not promise untested speed.

## Credential and data boundary

Dutchie read access and QBO write access are separate authorizations. Store credentials and client data outside Git. Limit collected personal data. Keep source retention consistent with approved terms and client authorization.

## Gates

Access and pricing → authorized one-month source test → report/METRC reconciliation → reviewed JE mapping → QBO sandbox test → authorized production pilot → larger periods/scheduling.

Existing reviewed JE files can support QBO-side development while Dutchie access is pending.

See [TODO.md](TODO.md).
