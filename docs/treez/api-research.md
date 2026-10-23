# Treez API Research

Research date: October 23, 2026
Scope: Public website documentation only. Initial use case: Five Lakes Farm sales extraction for METRC reconciliation, including periods up to 12 months. No API access requested or production data tested.

## Step 1 — API products and purposes

| Product | Documented purpose | Relevance |
| --- | --- | --- |
| SellTreez APIs | Operational POS integration; current reference divides APIs into dispensary-level and organization-level services. Ticket retrieval by close date supports pagination, JSON responses, and full_decimals. | Candidate for automated transaction extraction; historical completeness and field coverage remain untested. |
| AskTreez Retail Data API | Raw reporting data through DOMO, delivered as JSON for custom reports. Premium access with a cost; amount not stated on the reviewed page. Intended for retailers and some partners. | Candidate for accounting datasets. Compare coverage and price against SellTreez before selection. |
| AskTreez Market Data API | Anonymized market information for brands and partners. Inventory feed is restricted to consenting stores and relevant brands. | Its documented purpose does not fit complete client sales reconciliation. |

## Sources

- Developer home: https://code.treez.io/
- Getting Started: https://code.treez.io/docs/getting-started
- Current API overview: https://code.treez.io/reference/treez-api
- Partner onboarding: https://code.treez.io/page/partner-with-us
- Retail Data API: https://code.treez.io/docs/retail-data-api
- Market Data API: https://code.treez.io/docs/market-data-api
- Tickets by close date: https://code.treez.io/reference/ticket-get-by-close-date
- Current access instructions: https://support.treez.io/en/articles/9129351-requesting-api-access-for-treez-apis

## Additional observations

The Retail Data page names Ticketline, Inventory, and Payment tables as incrementally refreshed during the day; other tables refresh daily. It identifies last_retrieved_timestamp as a freshness check and recommends retrieving a day's complete available data the following afternoon. This is published guidance, not a tested completeness guarantee.

Some introductory and partner pages still describe legacy API keys. The current support article says new access uses V3 certificates from October 1, 2026 and legacy authentication/routes are deprecated November 1, 2026. It explicitly permits customer-maintained internal integrations. Whether our accounting firm's implementation qualifies under that route needs confirmation. Do not assume the separate DOMO Data API uses SellTreez authentication: its page describes client ID/client secret credentials, and applicability of the V3 transition to that service remains unconfirmed.

## Unresolved questions for subsequent research

- Historical coverage sufficient for a full calendar year, for each candidate API.
- Sales-line identifiers, historical METRC tags, and medical/adult-use license classification.
- Retrieval of existing returns, refunds, voids, and later corrections.
- Net Sales definitions and precision compared with existing reports.
- Available Retail Data tables, schemas, query limits, retention, and access price.
- Applicable internal-versus-partner access route for an accountant serving clients.

## Working assessment

Evaluate both SellTreez ticket extraction and Retail Data reporting. No API has been selected. Python extraction feeding Power Query remains a proposed implementation, subject to verified data coverage and validation against existing reports.

## Step 2 — Access requirements: support article review

Source: https://support.treez.io/en/articles/9129351-requesting-api-access-for-treez-apis
Evidence: Full article supplied by user on October 23, 2026; consistent with the previously reviewed official page.

### Confirmed from the article

- Treez permits approved third-party partners and customer-maintained internal integrations.
- New access uses V3 certificate-based authentication and self-signed JWTs. Treez assigns organization, dispensary, and endpoint permissions and provides the Organization ID.
- A registered partner certificate can cover additional authorized client organizations and dispensaries without a new certificate per client.
- For an existing registered partner, an authorized client user requests access through Treez's Need Help? > Chat with Support. Required details: customer URL, application/integration partner, customer contact name and email, and partner contact name and email. Existing Certificate ID may also be supplied.
- Treez verifies authorization and the registered certificate before configuring access. An unregistered partner must complete certificate registration first.
- Internal registration requires an RSA key pair, public certificate submission, and identification of the required organization, dispensary, and endpoints. Private keys must remain confidential and must not be supplied to Treez or committed to GitHub.
- Technical contact: api-support@treez.io or Treez Support.

### Not answered by this article

- Whether an outside CPA firm may develop and maintain an integration under a client's internal-integration authorization, or must become an approved partner.
- Partner onboarding/certification requirements specifically applicable to a read-only accounting integration.
- SellTreez access fees, setup fees, recurring fees, and minimum subscription requirements. Absence of pricing is not evidence that access is free.
- Availability of read-only permissions for all required endpoints.
- Whether the separate Retail Data API follows this certificate process.

These gaps are retained for the later consolidated action list. No client or vendor outreach has been performed.
