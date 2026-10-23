# Dutchie POS API — Staff Call Sheet

Prepared October 23, 2026. Initial research only; no call made.

## Initial access inquiry

Focus the first contact on CPA-firm eligibility, current access pricing, full-year sales/returns/correction coverage, and populated historical METRC package and selling-license information. This inquiry does not require a Journal Entry report, worksheet preparation or QuickBooks implementation. The broader technical questions below are follow-up material.


| Call detail | Record |
| --- | --- |
| Staff caller / date | |
| Dutchie representative / department | |
| Email / direct number / case number | |
| Client / product / locations | |
| Follow-up date | |

## Opening

> We are a CPA firm evaluating read-only access to authorized clients' Dutchie POS data. We want to automate daily sales preparation, reconcile transactions with METRC, and send reviewed journal entries to QuickBooks Online. We also need up to a full year of historical data. Please connect us with the API onboarding and reporting specialists.

Start with the client's Dutchie account representative or [official support](https://support.dutchie.com/hc/en-us). The [key request page](https://dutchie.com/business/api-key-open-access) is a later access step; a client's authorized account administrator must handle the request under Dutchie's process.

## Priority questions

| # | Question | Answer / evidence / follow-up owner |
| --- | --- | --- |
| 1 | Can our CPA firm maintain this integration under client-authorized internal use, or must we become a certified partner? How do we serve multiple clients? | |
| 2 | What are current setup, sandbox, production, per-location, per-firm and usage fees? What terms/support obligations apply? | |
| 3 | Which read-only endpoints give complete daily sales detail and financial controls for our intended workflow? | |
| 4 | Can we retrieve every transaction for a full year, including migrated/archived history? What is the earliest date? | |
| 5 | How do we retrieve full/partial returns, voids, deleted records and later corrections, including changes to prior periods? | |
| 6 | Which field identifies each historical METRC package tag and actual selling license? Does it remain available for depleted packages? | |
| 7 | How do API amounts reconcile to the Closing Report, including tax, discounts, rounding, tips, fees, deposits and tenders? | |
| 8 | What client approval and current Location/Integrator Key configuration do we need, and how are credentials delivered securely? | |

## Technical follow-up

- [ ] Confirm selected endpoints, parameter names, effective limits and supported date ranges.
- [ ] Confirm transaction-date/modified-date boundary behavior and business-day/timezone rules.
- [ ] Identify response caps/truncation and prove complete retrieval.
- [ ] Confirm stable location/transaction/line keys; preserve unaggregated detail.
- [ ] Explain historical tag/unit/license attribution and package splits.
- [ ] Provide return/void/correction examples and original-sale links.
- [ ] Explain Closing Report versions and supported historical cash controls.
- [ ] Supply sanitized JSON examples and exact report-to-API amount definitions.
- [ ] Explain key revocation/replacement and the Integrator Key enforcement schedule.
- [ ] Confirm permission to retain CPA workpapers and transfer approved summaries to QBO.
- [ ] Compare existing third-party accounting connectors on scope and price if appropriate.
- [ ] Optionally discuss MCP early access; confirm whether it supplies complete historical accounting data before considering it as an alternate source.

Staff need not solve coding details during the call. Ask the representative to route unanswered technical questions.

## Close

> Please send your recommended endpoints, current quote, access requirements and written answers to the historical coverage, returns and METRC tag questions. Please identify an owner and response date for anything outstanding.

| Next action | Owner | Due | Status |
| --- | --- | --- | --- |
| Written API/access recommendation | | | Open |
| Current quote and terms | | | Open |
| Technical answers and sanitized samples | | | Open |
| Client authorization and test reports | | | Open |
| James's review of scope/cost | | | Open |

Do not put keys or live client data in GitHub. No paid signup, contract acceptance or production posting is authorized by this call sheet.

References: [research](api-research.md), [action list](TODO.md), [pilot specification](extraction-specification.md).

## Research update — narrow the questions before calling

Public documentation now identifies the candidate package field, a scheduled Excel report route, an accounting-oriented Journal Entry report, published MCP pricing and key revocation. See the [research addendum](api-research.md#deeper-public-research--october-23-2026).

For question 6, ask whether the documented package identifier is populated historically and represents the actual Michigan METRC tag at sale, including depleted packages. Do not ask as though no package field is documented.

For question 2, distinguish POS API access costs from the separately documented MCP connection price. Ask about provisioned availability and relevant limits rather than asking Dutchie to repeat its MCP price.

Vendor contact is for unresolved eligibility, commercial terms and technical gaps; client samples and authorized tests can answer many validation questions.
