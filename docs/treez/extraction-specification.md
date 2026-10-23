# Treez Extraction Specification — Draft

Prepared October 23, 2026. This specifies desired outputs, not verified API capabilities. Read [research](api-research.md) and [action list](TODO.md). No production code or access is implied.

## Staff workflow

1. Select configured client/location/license and start/end dates (inclusive local reporting dates).
2. Run the extractor using a documented launcher or command. No routine Python editing.
3. Inspect the completion summary. An incomplete or failed run must not overwrite the last accepted dataset.
4. Refresh Power Query against a stable published output folder.
5. Review source controls, mapping exceptions, and reconciliation differences before acceptance.

Monthly, quarterly, and calendar-year windows up to 12 months must be supported after vendor historical coverage is confirmed. Proposed output: UTF-8 CSV tables with a schema/type dictionary; permitted source JSON stored separately and securely only where authorized. Staff-facing outputs should exclude unnecessary personal details and secrets.

## Required tables and row grain

All transactional tables include run_id, source_system, organization/location identifiers, source retrieval timestamp, and applicable source keys. License attribution must be sourced or explicitly recorded as verified configuration; do not infer it solely from patient type.

| Output | One row represents | Required content |
| --- | --- | --- |
| tickets.csv | One ticket's current extracted version | Source ticket ID, receipt number, original/refund linkage, status, payment status, source creation/close/update timestamps and offsets, reporting date, patient type, financial totals and fees |
| sales_lines.csv | One source ticket line | Ticket ID, stable line ID where verified, product/inventory references, source quantity and UOM, product contents, inventory type, source line amounts and normalization fields |
| line_taxes.csv | One tax component on one line | Ticket/line keys, tax ID/name, rate and amount |
| line_discounts.csv | One applied discount component | Ticket/line keys, discount ID/category/method, source amount, monetary savings, cart indicator and reward-dollar fields if available |
| payments.csv | One payment record | Ticket/payment IDs, method, amount, timestamp; no bank/card credentials |
| package_mapping.csv | One evidenced source inventory-to-package relationship | Location/license, inventory/retail identifiers, METRC tag, mapping source, retrieval time and historical validity where available |
| ticket_links.csv | One original/refund ticket relationship | Original ticket ID, refund ticket ID, link source and validation result |
| exceptions.csv | One unresolved extraction or mapping issue | Severity, issue code, source record key, explanation and required action |
| controls.csv | One comparable metric per period/location/license | API amount/count, report control, difference, precision basis and review status |
| manifest.json | One extraction run | Requested coverage, API/version, configuration/schema version, start/end/retrieval times, per-date/page counts, retries/errors, row counts, output hashes and completion status |

Do not expand taxes, discounts, payments and package mappings together into a sales table: multiple child arrays can multiply revenue. Preserve unmapped sales lines in output and report mapping failures rather than dropping them through inner joins.

## Keys and types

- Keep ticket IDs, tags, receipts, licenses and inventory identifiers as text. Source IDs are qualified by organization/location as appropriate.
- Treat items[].id as a candidate line key until uniqueness and persistence are tested. An array ordinal can preserve source position for traceability, but is not a proven stable business identifier. Never deduplicate by timestamp, tag, quantity or price alone.
- Preserve monetary values with decimal-safe parsing and documented precision; output invariant decimal notation. Avoid early rounding and double subtraction of discounts.
- price_sell is documented as the line amount across units, not a unit price. Validate against actual records before choosing a canonical Net Sales field.
- Retain source quantities/units separately from converted values. Bulk quantity may already be grams; packaged quantity may be units. Conversion rules require product/UOM evidence, never an unconditional quantity-times-weight formula.
- Preserve timestamps with offsets, plus UTC and explicitly derived local reporting dates where needed. Confirm timezone/day cutoff and daylight-saving behavior before use.
- Missing values remain distinguishable from zero. Preserve unknown status/category values and flag them for review.

## Extraction integrity

- Every requested date and every page must either complete or be listed as failed; an empty response is not equivalent to a failed call.
- Use validated pagination termination and sorting rules, bounded retries, throttling, and restart checkpoints. Do not assume the first page is zero or one.
- Maintain separately retained run outputs and publish a stable accepted folder only after integrity checks pass. Power Query must not consume a partially updated set of tables.
- Repeated runs replace the current logical record/version under verified source keys rather than accumulate duplicate revenue. Retain permitted prior evidence separately for traceability.
- Incremental refresh uses an explicit overlap and deduplication strategy after update semantics are verified. Track uncovered intervals, deleted records and lookback expiration.

## Review presentation in Excel

Proposed review tabs: Run Status; Source Controls; Sales Detail; Returns; METRC Mapping Exceptions; Reconciliation Exceptions. These are design targets, not created workbook tabs.

- Run Status shows coverage, freshness and failures prominently.
- Source Controls separates gross sales, discounts, returns, net sales, tax, fees and tenders, with the exact report/filter/precision basis.
- Exceptions distinguish failed extraction, missing tags, ambiguous mapping, unknown UOM/status, identifier collisions and unexplained monetary differences.
- Rounded receipt/cash controls and unrounded Product Report controls are compared separately with a documented rounding bridge.

## Acceptance gates

1. Vendor confirms authorized access, terms, relevant fields and required history.
2. An initial month agrees to the appropriate source controls with every material/unexplained difference resolved or explicitly retained for review.
3. Test cases cover same-timestamp/tag distinct sales, multi-quantity lines, bulk/package units, loyalty/cart discounts, full/partial and cross-month returns, voids/cancellations and later corrections.
4. Mapping tests include depleted/archived stock and multiple retail IDs per tag; uncertain mappings remain exceptions.
5. Rerun, restart, incremental overlap, year-end and daylight-saving tests demonstrate no missing/duplicated records.
6. Full-year extraction and controls pass before manual downloads are retired. CSV import remains supported as fallback.

## Unresolved API mapping

All canonical field mappings remain provisional. In particular: historical line-to-METRC join, stable line ID, selling license, return signs/dates, subtotal fees, reward dollars, API precision/report equivalence, retention and pagination rules. Resolve these with vendor answers and sanitized authorized samples before implementation.
