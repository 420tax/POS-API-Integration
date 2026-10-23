# Dutchie POS API Research

Research date: October 23, 2026. Scope: public official documentation only. No client access, credentials, paid signup, live extraction or QuickBooks posting performed.

## Purpose and proposed route

Evaluate read-only Dutchie POS extraction for daily sales journal entries, sales/METRC reconciliation and periods up to 12 months. The proposed workflow is Dutchie source data → validated accounting tables → staff review → separately authorized QuickBooks Online posting. This is a design proposal, not a working integration.

Use the **Dutchie Point of Sale API** for investigation. An online menu/e-commerce connection alone should not be presumed to contain all in-store accounting activity. Confirm the client's actual product, locations and licenses before requesting access.

## Access and eligibility

The [official key-request article](https://support.dutchie.com/hc/en-us/articles/27660267271187-Dutchie-POS-API-key-request-process-for-third-party-integrations) says:

- Only an authorized account administrator may request keys; support does not issue them by phone or chat.
- Customers may request read-only keys for internal use.
- Third-party partners have a certification/approval route. The article estimates three business days for approved-integrator key requests.
- Keys are described as non-expiring. Ask about revocation and replacement after compromise rather than treating non-expiration as a security plan.

[Customer API request page](https://dutchie.com/business/api-key-open-access). The older support form link redirects here. Do not submit until the applicable route is clear.

**Unresolved:** Whether a CPA firm developing and maintaining an extractor for multiple authorized clients qualifies under customer internal use or needs partner approval. Obtain written confirmation, current fees, sandbox arrangements and an endpoint permission list.

## Authentication discrepancy

The [standalone authentication guide](https://api.pos.dutchie.com/pages/authentication.html) describes Basic Authentication with an API key as username and an empty password.

The [live API specification](https://api.pos.dutchie.com/swagger/v001/swagger.json) instead describes a Location Key as username and an Integrator Key as password, currently optional but intended to become mandatory. Confirm the current requirement and enforcement date with Dutchie. Test only with authorized credentials. Never put keys, encoded Authorization values or client datasets in Git.

## Endpoint evidence from the live specification

| Candidate | Published behavior |
| --- | --- |
| GET /reporting/transactions | Transaction-date or modified-date filters, mutually exclusive with transaction-ID lookup; IncludeDetail and RollupLineItems options. |
| GET /reporting/register-transactions | Register activity, not solely product sales. |
| GET /reporting/closing-report | Financial summaries; request interval 12 hours–31 days; V1/V2 configurations. |
| GET /reporting/cash-summary | Seven-day lookback restriction. |

Published transaction schema includes return/void indicators, original-transaction links, medical classification and rounding fields. Line identifiers are not guaranteed unique outside their transaction. Use a location/transaction/line composite candidate key and verify persistence. Preserve unaggregated detail; confirm RollupLineItems=false.

The specification lists 120/min for register-transactions and closing-report, 600/min for transactions and 480/min for cash-summary. These endpoint values differ from the general guide; verify effective limits. No complete-year guarantee or proven historical sales-line-to-METRC-tag join was established.

## JSON, Python and Excel

The [API overview](https://api.pos.dutchie.com/pages/overview.html) describes REST access with JSON responses. Python can act as an HTTP client; Python is our proposed implementation choice, not an asserted vendor requirement or official Dutchie Python SDK endorsement.

Preserve permitted JSON source evidence; generate stable CSV tables for Excel/Power Query where useful. CSV-to-JSON conversion does not add missing information. Keep transactions, lines, taxes, discounts and tenders separate to prevent multiplied totals.

Staff should select client and date range through a simple launcher or interface. Routine use must not require editing Python. Development of the earlier worksheet utility remains paused; this research does not restart it.

## Dates, completeness and extraction controls

[Incremental-sync guidance](https://api.pos.dutchie.com/pages/incremental-sync.html) documents modified-date filters, UTC filtering, overlapping recovery and advancing checkpoints only after successful extraction. It warns that deleted records typically are not exposed. Therefore, incremental retrieval alone does not establish completeness.

[Pagination guidance](https://api.pos.dutchie.com/pages/pagination.html) describes register-transactions as date-filtered without pagination. Do not invent page parameters or assume a successful large response is untruncated. Ask for response caps, supported date-window sizes, boundary inclusivity and completeness controls for each selected endpoint.

The [rate-limit guide](https://api.pos.dutchie.com/pages/rate-limits.html) gives general tiers including 60/min for reporting and recommends backoff for HTTP 429. Prefer verified endpoint-specific constraints and record discrepancies. Capture request windows, counts, errors and extraction timestamps.

## Pricing and terms

No dollar quote for this firm's intended access was established in reviewed sources. “Open Access” is not a confirmed promise of free production access.

The [Developer Terms](https://dutchie.com/business/legal/developer-terms) require customer permission and address privacy, security, data retention/deletion, permitted uses, fees and ordering documents. Ask Dutchie to confirm CPA workpapers, METRC comparisons, QBO transmission, backups, retention after access ends, and whether restrictions involving partner services affect this workflow. Review the applicable terms before commitment. This is a research summary, not a legal conclusion or acceptance.

## QuickBooks and alternate connections

[Official QuickBooks integration article](https://support.dutchie.com/hc/en-us/articles/17139247079059-QuickBooks-integration-Dutchie-POS-Backoffice) says Dutchie POS has no native QuickBooks integration and names Racetrack by Palomino, Armanino and Bookkeep as third-party options. Compare capabilities and costs if custom development is unattractive; none has been selected or tested.

[Dutchie MCP support article](https://support.dutchie.com/hc/en-us/articles/53914774237843-Dutchie-MCP-what-it-is-and-how-to-connect-your-AI-assistant) describes an early-access, read-only AI connection coordinated through the account/sales team. [Setup documentation](https://docs.dutchie.com/dutchie-core-docs/dutchie-core-docs/dutchie-pos-mcp/getting-started/connect-your-assistant) describes a separate bearer MCP key. This does not prove full-year accounting export coverage, and MCP access is not the POS API key. Treat it as a separate optional investigation.

## Decision and remaining evidence

The reporting API is promising for replacing manual report downloads and supplying daily sales preparation. Selection requires access eligibility, price, complete historical coverage, stable identifiers, historical METRC package/license attribution, full returns/correction handling and reconciled report totals.

Before QBO posting, separately validate account/class/location mappings, daily balance, duplicate prevention, failed/uncertain request recovery and retained QuickBooks transaction IDs. Do not assume Dutchie permissions authorize QuickBooks writes.

See [action list](TODO.md), [call sheet](call-sheet.md) and [pilot specification](extraction-specification.md).

## Research limitations

The public specification was readable through web retrieval. A direct programmatic download attempt returned non-JSON and could not be parsed; no downloaded schema or SDK was generated. Standalone guides and the live specification differ in authentication and limits. Those are unresolved documentation discrepancies, not tested behavior. No production data was accessed.
