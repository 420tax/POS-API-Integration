# Dutchie Integration — Action List

Prepared October 23, 2026. Owners are proposed roles, not assigned people. No outreach or commitments made.

## Completed public research

- [x] Identify POS API, JSON responses and public reference.
- [x] Review customer/internal versus certified-partner access.
- [x] Identify transaction, closing and register reporting candidates.
- [x] Record authentication/limit discrepancies and historical coverage gaps.
- [x] Identify existing third-party QuickBooks routes and optional MCP.
- [x] Prepare [research](api-research.md), [call sheet](call-sheet.md) and [pilot specification](extraction-specification.md).

## 1. Establish eligible access and price

Owner: James/designated staff. Method: client's Dutchie account representative or official Support portal; request API onboarding/technical specialist.

- [ ] Explain CPA firm, read-only client extraction, METRC reconciliation and reviewed daily sales entries for QBO.
- [ ] Confirm internal-use versus certified-partner route, including multiple clients.
- [ ] Obtain written setup/sandbox/production/per-location/per-firm fees, limits, minimum terms and support terms.
- [ ] Confirm current Location/Integrator Key requirements and transition deadline.
- [ ] Obtain exact read-only endpoint permissions; do not request POS write access.
- [ ] Confirm permitted workpaper retention, normalization, METRC comparison and QBO transmission under applicable terms.
- [ ] Ask about third-party accounting integrations as a cost/maintenance comparison.

Evidence: written eligibility determination, scoped endpoints, current quote and applicable agreement. James reviews commitments.

## 2. Resolve technical gaps

Owner: staff coordinates; technical implementer reviews. Method: send call-sheet questions and request written answers/sanitized examples.

- [ ] Confirm earliest history, migrations, full-year extraction and archived records.
- [ ] Confirm transaction-date versus modified-date filters, timezone/business day, inclusive/exclusive boundaries and supported windows.
- [ ] Confirm response caps/truncation, timeout handling and completeness checks for each endpoint.
- [ ] Confirm effective rate limits, retry rules and current specification.
- [ ] Prove transaction/line identity across locations, corrections, returns and unaggregated output.
- [ ] Identify historical METRC tag, quantity/unit and selling-license fields/joins; test depleted packages and mixed medical/adult configurations.
- [ ] Define refunds/voids/deletions/corrections, signs, original links and cross-period recognition.
- [ ] Map gross/discounts/net/taxes/fees/tips/tenders/rounding to the client's Closing Report.
- [ ] Confirm cash-summary historical limitations and equivalent historical controls.
- [ ] Obtain sanitized completed/discounted/weighted/multi-tender/partial-return/void samples and report V1/V2 guidance.

## 3. Client authorization and controls

Owner: James/staff and client's authorized Dutchie administrator.

- [ ] Select pilot client, exact Dutchie product, locations/licenses and QBO company.
- [ ] Obtain express client authorization for extraction and any data transfer.
- [ ] Have authorized administrator request scoped keys using Dutchie's current process after access route is confirmed.
- [ ] Keep credentials and production data in approved secure storage outside Git.
- [ ] Obtain one month's Closing Reports, transaction exports, tender/settlement controls, METRC data and existing SaaSant JE output.
- [ ] Record report filters, business-day rules and mapping rules, including the existing two-JE workflow where applicable.

## 4. Build only an authorized small pilot

Owner: technical implementer; staff operate and James reviews.

- [ ] Test location identity and minimum read permissions.
- [ ] Implement bounded date-window extraction, decimal-safe parsing, retries, checkpointing and manifest.
- [ ] Retain separate child tables; avoid line rollups and duplicate joins.
- [ ] Reconcile one month to existing reports and METRC; keep exceptions visible.
- [ ] Validate full-year retrieval only after one-month acceptance.
- [ ] Provide simple staff controls; no routine Python editing.

## 5. Separate QBO posting pilot

Owner: technical implementer with James's accounting mapping/review.

- [ ] Investigate current Intuit app eligibility, authentication, costs and sandbox setup separately.
- [ ] Use existing reviewed daily JE output first if that accelerates testing; Dutchie API access need not block QBO-side design.
- [ ] Map exact accounts, classes/locations where used, dates, descriptions and entry structure.
- [ ] Validate balanced entries and source totals before submission.
- [ ] Implement a local posting register with company/location/date/entry-type identity; detect prior imports and uncertain requests.
- [ ] Preview entries for review; test in a sandbox before separately authorized production posting.
- [ ] Record QBO transaction IDs, successes/failures and read-back verification; never retry an uncertain write blindly.
- [ ] Compare staff handling time and results with SaaSant before replacing it.

## Later

- [ ] Evaluate scheduled runs only after reliable staff operation.
- [ ] Evaluate MCP separately if useful for read-only analysis; do not assume it replaces complete export.
- [ ] Retain manual CSV imports as fallback.

Return vendor answers to this repository as approved nonconfidential summaries. Keep client data, credentials and confidential quotes outside Git.

## Additional public research and work available without a call

- [x] Identify a direct state-tracking package field; see research addendum.
- [x] Establish published no-extra-charge MCP pricing separately from POS API pricing.
- [x] Identify scheduled Excel Closing Reports and the existing Journal Entry report.
- [x] Establish published API-key revocation route in merchant terms.
- [ ] Compare client samples of Journal Entry and Closing Reports with existing daily JE output.
- [ ] Evaluate scheduled report delivery as an interim extraction method.
- [ ] Map documented candidate fields before vendor outreach; use authorized testing to resolve sample-dependent gaps.
- [ ] Keep questions about populated historical values, actual permissions and full-year completeness open until observed.

The public review does not require a call before all further progress. Read the research addendum before using the original question list.
