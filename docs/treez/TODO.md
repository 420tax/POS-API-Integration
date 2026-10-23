# Treez Integration — Action List

Prepared October 23, 2026. Research: [api-research.md](api-research.md).

Status: Public-documentation review completed to the extent accessible. Vendor answers and authorized test access are now required. Proposed owners below are roles, not assigned individuals. No outreach or commitments have been made.

## 1. Establish access route and actual price

Owner: James or designated staff researcher.
Method: Email partners@treez.io for commercial/onboarding questions; request a call if necessary and obtain written confirmation afterward. Describe a CPA firm extracting authorized clients' sales for accounting and METRC reconciliation, initially Five Lakes Farm; read-only use, up to 12 months. Consult api-support@treez.io for technical questions and asksupport@treez.io for Retail Data specifics. Do not submit a paid application or accept agreements until James reviews the actual proposal.

- [ ] Ask whether the firm must become a partner or may maintain a client-authorized internal integration; ask how multiple clients are authorized.
- [ ] Obtain separate written quotes for SellTreez and Retail Data: setup, sandbox, production, per firm/client/location/endpoint charges, minimum terms, call allowances and overages.
- [ ] Clarify whether January 2025 Exhibit B remains current and how client_id billing maps to V3 certificates. Is the $500/month sandbox required, and when does billing end?
- [ ] Ask whether ticket/package/tag lookup endpoints require paid Inventory/Stock access and exactly which fee applies.
- [ ] Obtain current agreements/onboarding and read-only certification requirements. Confirm authorized local extracts, normalization, Excel/Power Query outputs, workpaper retention and backups after access ends, and applicable privacy/support obligations.

Completion evidence: Current written access determination, scoped endpoint list, quote, and applicable terms. Store confidential commercial material outside public Git; summarize approved nonconfidential decisions here.

## 2. Resolve technical questions before selecting an API

Owner: Staff researcher coordinates vendor responses; technical implementer reviews.
Method: Send the questions below to api-support@treez.io; route Retail Data schema questions to asksupport@treez.io. Request a technical call only where written answers are insufficient.

- [ ] Can close-date retrieval return every historical ticket for the requested full calendar year? What is the oldest available date? Does the 30-day last-updated limit apply to V3?
- [ ] Which endpoint and status/date rules retrieve completed sales, full and partial returns, voids, removed tickets, cancellations, and corrections? How are returns dated and signed, and can original/refund records be enumerated completely?
- [ ] Is items[].id stable and unique within a ticket or globally? Does it survive edits, returns, or package splits? Does each returned item correspond to one sales line and package?
- [ ] Which ticket field joins to retail_id and then the METRC package label? Can depleted/archived packages and historical tag changes be resolved as of sale? Request examples of one-to-many mappings and split packages.
- [ ] Which field identifies the actual selling license and medical/adult classification at sale, including mixed inventory or license configurations?
- [ ] Request current V3 completed medical-sale, discounted/loyalty-sale, multi-line, weighted-product and partial-refund samples; sanitized samples only in Git.
- [ ] Obtain definitions for price_sell, sub_total, fees, reward_dollars and refund amounts; explain the published subtotal/fee discrepancy and map API fields to the exact Net Sales/Product Report used by Five Lakes.
- [ ] Confirm timezone, business-date cutoff, daylight-saving handling, refund recognition date and METRC timestamp relationship.
- [ ] Confirm starting page, maximum page size, sort order, total-count/last-page signals, consistency while records change, rate limits, 429/retry behavior and incremental checkpoint inclusivity.
- [ ] Clarify whether every relevant change updates last_updated_at; whether ticket history contains value snapshots or only events; whether deleted records remain discoverable.
- [ ] For Retail Data: obtain current credentials method, table dictionary, sample queries, historical retention, query/pagination limits, freshness markers, refund/deletion handling and complete store/date filtering. Request an accessible Postman collection.
- [ ] For V3: resolve two-part authorization serialization, Base64 variant, audience URL, private-key PEM format, exact TTL, clock tolerance, certificate rotation/revocation and read-only permission validation.

Completion evidence: Answers or explicitly accepted limitations for every question needed by the chosen route. Do not label untested vendor claims as observed behavior.

## 3. Obtain client authorization and control reports

Owner: James/staff with the authorized Five Lakes Farm contact.
Method: Contact Five Lakes Farm after route and proposed costs are clear. Identify its authorized Treez administrator; use the client's approved secure channel for identifiers/data.

- [ ] Confirm location URL, relevant legal entity/license(s), extraction period and authorized client contact.
- [ ] Confirm existing Treez subscription/API entitlements and whether historical data spans system migrations.
- [ ] Obtain approval for the selected scope and costs.
- [ ] If partner route: have the authorized client user request access through Need Help? > Chat with Support, supplying customer URL, integration name, both contact names/emails and registered Certificate ID where applicable.
- [ ] Secure one month's existing Treez exports, report names/filter settings and control totals, plus matching METRC data. Include known repeat timestamp/tag sales, discounts, weighted items and returns. Keep production data outside Git.

Completion evidence: Client authorization, access granted to correct organization/location/endpoints, and test period/control totals secured.

## 4. Build a small authorized extraction pilot

Owner: Technical implementer; James/staff review results.
Method: Implement only after the preceding decision gates pass. AI-assisted implementation is appropriate, but staff need a documented, reproducible operating procedure.

- [ ] Select an approved execution computer and credential store; generate/register public certificate only if required. Keep private keys and live configuration outside Git.
- [ ] Test authorization and endpoint permissions without writes to POS. Avoid ticket preview/create/update and inventory mutations.
- [ ] Implement date selection, all-page retrieval, throttling, bounded retry/backoff, resumable checkpoints, and explicit failure reporting. Empty responses must be distinguished from failed requests.
- [ ] Use decimal-safe amounts; retain original precision and timezone offsets. Preserve permitted source evidence securely and omit unnecessary personal/secret fields from outputs and logs.
- [ ] Produce separate tickets, sales lines, taxes, discounts, payments and package mapping tables, with documented keys, units and schema version. Do not create duplicated revenue through one-to-many joins.
- [ ] Supply a simple launcher or command with client/start/end inputs, clear success/failure messages and an extraction manifest. Staff should not edit Python during routine use.

Completion evidence: A reproducible one-month extraction with request/page counts, row counts, dates, errors and source/output mappings.

## 5. Validate before replacing manual downloads

Owner: Staff prepares comparisons; James reviews unexplained differences.

- [ ] Compare ticket/line counts, gross sales, returns, discounts, net sales, tax, fees and tenders against the same location/license/date report controls.
- [ ] Explain rounded receipt/cash versus unrounded Product Report differences separately; do not use an arbitrary tolerance to hide discrepancies.
- [ ] Trace sale-to-METRC tag joins, unmapped rows, multiple matches, units and medical/license attribution. Check known duplicate timestamp/tag sales remain distinct.
- [ ] Test partial/full refunds, cross-month returns, later corrections, canceled/removed records and weighted/package quantity cases.
- [ ] Rerun the identical period and prove no duplicate accumulation. Test incremental overlap and an interruption/restart without gaps.
- [ ] Test month-end/year-end and daylight-saving boundaries. Validate full-year extraction and control totals after one-month acceptance.
- [ ] Document limitations and obtain review sign-off before retiring manual CSV downloads. Keep CSV import as a supported fallback.

Completion evidence: Reviewed reconciliation with explained differences, retained exceptions and a documented repeatable procedure.

## Later enhancements

- [ ] Evaluate scheduled extraction after staff can operate the pilot reliably.
- [ ] Consider webhooks only as a supplement; ordinary Ticket Webhooks omit cancellation/deletion triggers. Confirm status/refund coverage, retries and reconciliation recovery before use.
- [ ] Reuse the approved output specification across POS platforms. Keep platform integration code in this repository and coordinate reusable Excel reconciliation skill work separately.

## Immediate handoff

Next human action: James or designated staff should contact Treez using sections 1–2. API selection, paid signup, client access provisioning and live completeness testing cannot be completed from public documentation alone.

## Preparation completed while vendor outreach is pending

- [x] Draft desired output tables, staff workflow, data types and acceptance checks: [extraction-specification.md](extraction-specification.md).
- [ ] After vendor answers arrive, map verified API fields to this specification and resolve the listed gaps before coding.

Vendor/client contact tasks above remain open; recording this specification does not mean access or integration testing is complete.

## Offline CSV preparation pilot completed

- [x] Locate existing Treez/METRC workbook and inspect actual source headers.
- [x] Build preparation utility and Windows prompted launcher: [pilot instructions](../../tools/treez/csv-preparation/README.md).
- [x] Process all five populations without modifying source workbook or silently removing nonblank records; independently verify output counts.
- [x] Test distinct sale preservation, decimal text, failure reporting and refusal to overwrite runs.
- [ ] Staff/James: test launcher on the intended Windows computer after Python/openpyxl are configured. Provide any error message; no Python editing required.
- [ ] Review Non-METRC preparation issues before treating those rows as clean transactions; review December 25 no-activity date against store records.
- [ ] Obtain original monthly Treez CSV layout before implementing a raw monthly-file append/coverage feature; the current CSV route expects already-combined population files.
- [ ] Continue transaction reconciliation separately; the preparation pilot does not match records or establish API field equivalence.

See [validation](../../tools/treez/csv-preparation/validation.md). API access remains dependent on vendor/client tasks, but offline preparation has now been implemented and exercised with existing data.
