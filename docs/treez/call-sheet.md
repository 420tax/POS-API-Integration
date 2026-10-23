# Treez API — Staff Call Sheet

Prepared: October 23, 2026  
Project: Five Lakes Farm sales, METRC and accounting reconciliation  
Status: Call preparation only; no contact, access request or purchase recorded.

## Call details

| Item | Record |
| --- | --- |
| Staff caller | |
| Call date/time | |
| Treez representative and department | |
| Representative email/direct phone | |
| Support case or reference number | |
| Follow-up date | |

## Purpose and opening statement

> I am calling on behalf of James Campbell, LLC, the CPA firm assisting Five Lakes Farm. We want read-only access to Treez sales data for reconciliation with METRC and accounting records, including periods up to a full year. We are evaluating the SellTreez V3 Ticket API and the Retail Data API. We need to confirm which service provides complete historical sales lines, returns and corrections, and connects each sales line to its historical METRC package tag. We also need the current access requirements and pricing.

Our initial preference is to evaluate **SellTreez V3 Ticket API access**, including tickets by close date and by last updated date, plus any necessary read-only package/tag lookups. This is a candidate, not a final API selection. Ask Treez to compare the Retail Data API if it offers better historical accounting coverage.

## Who to contact

| Topic | Published contact | Request |
| --- | --- | --- |
| Eligibility, onboarding and pricing | partners@treez.io | Commercial/onboarding representative |
| V3 access, endpoints and authentication | api-support@treez.io | Technical API representative |
| Retail Data tables and reporting coverage | asksupport@treez.io | Retail Data specialist |

These are published email contacts, not verified telephone numbers. If a call is preferred, request the correct number or a scheduled call. If one representative cannot answer, obtain the correct contact and a case/reference number.

## First call — obtain these answers first

Record answers in the table. Ask for written confirmation and supporting documentation.

| # | Ask Treez | Answer / evidence / person responsible |
| --- | --- | --- |
| 1 | May an outside CPA firm operate a read-only integration for authorized clients, or must we become an approved partner? Can one firm registration serve multiple clients? | |
| 2 | For this reconciliation, do you recommend SellTreez V3 Ticket API or Retail Data API, and why? Which exact endpoints or tables are required? | |
| 3 | Can we retrieve a complete historical year? Our initial test data covers October 1, 2025–September 30, 2026; we also need calendar-year extraction. What is the oldest available date, and are archived records included? | |
| 4 | Does read access include full and partial refunds, returns, voids, cancellations, deleted/removed tickets and later corrections? How do we retrieve each category and link refunds to original sales? | |
| 5 | How does each historical sales line connect to the METRC package tag used at sale? Identify the exact fields and joins, including depleted/archived packages, splits and multiple tags. | |
| 6 | Which field identifies the actual selling license and medical/adult-use classification at the time of sale? | |
| 7 | What is the complete current price for each option: setup, sandbox, production, per firm/client/location/endpoint fees, minimum term, included calls and overages? Are package/tag lookups an additional paid service? | |
| 8 | What client authorization, agreements, approval, sandbox testing and certificate registration are required before read-only production access? | |

If time is limited, prioritize questions 1–7 and arrange a technical follow-up. Do not treat an unanswered question as a negative answer.

## Technical follow-up

The staff caller may send this section to the technical representative. Staff do not need to resolve implementation details during the call.

### Historical extraction and updates

- [ ] Confirm current V3 limits: maximum page size, first page number, rate limit per location, sort order and reliable last-page/total-count indicator.
- [ ] Confirm whether the documented 30-day lookback restriction for last-updated retrieval applies to V3. Distinguish this from close-date historical access.
- [ ] Explain whether every relevant correction changes the last-updated timestamp and how changes to older tickets are retrieved.
- [ ] Explain deletion discovery, checkpoint inclusivity and how pagination remains complete while tickets change.
- [ ] Confirm timezone, business-day cutoff, daylight-saving handling and the recognition date for cross-period returns.

Answer / documentation:

> Pending.

### Sales fields and control totals

- [ ] Confirm stable ticket and line identifiers, their uniqueness scope and behavior after edits or returns.
- [ ] Provide definitions for quantities and units, gross sales, discounts, loyalty rewards, net sales, taxes, fees and payment amounts.
- [ ] Identify the API fields/calculation that reconcile to Five Lakes Farm's existing Net Sales/Product Report.
- [ ] Confirm what `full_decimals` preserves and how report amounts differ from rounded receipts and tenders.
- [ ] Supply sanitized examples: medical sale, adult-use sale, discounted/loyalty sale, weighted product, multiple lines, partial refund and later correction.

Answer / documentation:

> Pending.

### Access and authentication

- [ ] Confirm read-only permissions for the exact required endpoints, including package/tag lookups.
- [ ] Provide current V3 authentication instructions and a working Python example.
- [ ] Resolve the documented examples' two-part authorization format, Base64 variants, audience URL and exact 30-second TTL.
- [ ] Confirm certificate registration, Organization ID, dispensary identifier, certificate rotation/revocation and testing procedure.
- [ ] Explain secure delivery of access information. Only the public certificate is provided to Treez; the private key stays with the firm.

Answer / documentation:

> Pending.

### Retail Data alternative

- [ ] Provide the current table dictionary and sample queries for Ticketline, Payment and any package/license mapping tables.
- [ ] Confirm historical retention, refund/correction/deletion coverage, store/date filters, pagination/query limits and refresh/completeness markers.
- [ ] Confirm its current authentication method separately from SellTreez V3.
- [ ] Provide an accessible Postman collection and a separate written price quote.

Answer / documentation:

> Pending.

### Agreements and permitted accounting use

- [ ] Confirm permission for local extracts, normalization, Excel/Power Query reconciliation and CPA workpapers.
- [ ] Clarify retention of source extracts, derived workpapers and backups after API access ends.
- [ ] Confirm support, privacy and certification obligations applicable to a staff-operated accounting extractor.
- [ ] Ask whether the January 2025 published fee schedule still applies, including its sandbox charge; request the current order form. Do not assume it is a current production quote.

Answer / documentation:

> Pending.

## Request before ending the call

> Please email your recommended API, the required endpoints or tables, written answers to the historical coverage and METRC tag questions, current pricing, and the access/onboarding steps. Please identify any questions that need another department and who will follow up.

- [ ] Record representative name, email and case number.
- [ ] Obtain owner and expected response date for every unresolved priority question.
- [ ] Request written answers, current quote, applicable agreements and sanitized samples.
- [ ] Confirm the next meeting or follow-up date.

## Client information to obtain when the access route is clear

Use the client's approved secure channel.

- [ ] Confirm the relevant location URL, legal entity, medical/adult-use licenses and authorized Treez administrator.
- [ ] Confirm requested extraction dates and any system migrations affecting history.
- [ ] Obtain client authorization for the selected scope and cost.
- [ ] If Treez requires a client support request, have the authorized client user submit it through Need Help? > Chat with Support, following Treez's current instructions.
- [ ] Obtain one month's matching Treez reports/control totals and METRC data for validation.

## Call outcome and next actions

**Recommended API and reason:** Pending.  
**Required endpoints/tables:** Pending.  
**Historical coverage confirmed:** Pending.  
**Historical METRC tag mapping confirmed:** Pending.  
**Total proposed cost and billing basis:** Pending.  
**Access route and client authorization:** Pending.  
**Remaining blockers:** Pending.

| Action | Owner | Due date | Status / evidence |
| --- | --- | --- | --- |
| Obtain written Treez response and quote | | | Open |
| Review access route, terms and costs with James | | | Open |
| Obtain client authorization and control reports | | | Open |
| Resolve remaining technical questions | | | Open |
| Plan authorized one-month extraction and reconciliation test | | | Open |

James reviews paid applications, agreements and costs before commitment. Successful API responses alone do not prove completeness; validate against source reports before replacing manual downloads. Keep credentials and live client data outside GitHub.

## Project references

- [Research and official source links](api-research.md)
- [Project action list](TODO.md)
- [Proposed extraction specification](extraction-specification.md)
- [Treez authentication documentation](https://code.treez.io/reference/authentication)
- [Retail Data API documentation](https://code.treez.io/docs/retail-data-api)
