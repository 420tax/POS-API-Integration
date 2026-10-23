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

## Step 2 continued — Published partner onboarding

Source: https://code.treez.io/page/partner-with-us
Evidence: Page text supplied by user on October 23, 2026.

The published SellTreez partner process requires:

1. Submit a partner application: https://www.treez.io/partner-application
2. Sign an MNDA and API Usage Agreement: https://code.treez.io/page/legal
3. Receive sandbox access after signing the agreements.
4. Provide proof of client support resources and documentation.
5. Complete the Partner Survey: https://docs.google.com/forms/d/e/1FAIpQLSdposbpvof4pacDD9cmV4Dd95KXHAuk3QHeDAiEeZqBTdspCQ/viewform?usp=sf_link
6. Obtain approval before clients request production access.

Treez advises developing and testing in the sandbox before requesting production access. This page does not describe detailed certification test criteria or state fees. Although its heading mentions both SellTreez and Data API access, the listed procedure is explicitly labeled SellTreez; do not assume identical requirements for the Retail Data API.

Documentation discrepancy: The page still says customers request an API Key after approval and links to an older support article. Current access guidance instead requires V3 certificate registration and authorization. Preserve the onboarding requirements as published, but use current V3 guidance for authentication; ask Treez to confirm the current onboarding sequence.

Next website research: Read the API Usage Agreement for eligibility, permitted accounting use, client authorization, fees, data handling, and support obligations. No agreements have been accepted and no application or survey has been submitted.

## Step 2 continued — API Usage Agreement and published fees

Source: https://code.treez.io/page/legal
Evidence: User-supplied agreement text and official page reviewed October 23, 2026. Findings below describe published terms, not acceptance of them or a determination of enforceability.

Exhibit B is labeled January 2025. These are published historical schedule amounts, not a current quote for our proposed integration:

| Item | Published charge |
| --- | --- |
| Development environment | $500/month per client_id |
| Stock API premium access | $200/month per client_id per unique instance |
| Invoice API premium access | $100/month per client_id per unique instance |
| Usage beyond initial 100,000 monthly calls | $25 per additional 100,000 calls |

Section 4.7 also references the applicable Order Form. Confirm current V3 pricing, how client_id maps to V3 registration, overage billing increments/aggregation, whether sandbox charges continue after development, and whether internal read-only integrations have different terms. Do not treat $500 as a confirmed production-access fee or assume Stock/Invoice endpoints are required for this project. Retail Data API pricing remains unresolved.

Relevant published provisions for follow-up:

- Sections 2.1 and 5.1 restrict permitted data use/storage and require strong encryption for stored data; personal information has additional consent restrictions.
- Section 4.5(h) restricts extracting data to enhance third-party data files without prior written consent; 4.5(l) restricts modification of Customer Data. Obtain express confirmation of permitted local normalization, Excel/Power Query reconciliation, and CPA workpaper outputs rather than assuming these provisions prohibit or authorize our workflow.
- Sections 5.2 and 7.4 address deletion at termination; 5.2 contains a law/government-obligation exception while 7.4 does not restate it. Clarify retention of source extracts, derived reconciliations, workpapers, and backups after API access ends.
- Section 4.8 and section 12 place application operation/support responsibilities on the integrator. Section 9 requires a user agreement and privacy policy when offering an application outside the organization. Applicability to a staff-operated accounting extractor remains to be confirmed.
- Section 6.2 specifies security-incident reporting within three business days. Section 15.8 contains a non-publicity provision; clarify permission for any future public integration announcements or distribution. Current research records publicly available documentation, not a claim of approved partner status.

Accountant eligibility remains unanswered. These matters belong in the later vendor question/action list. No agreement has been signed or accepted; no credentials or client datasets have been committed.

## Step 2 continued — Retail Data API access

Source: https://code.treez.io/docs/retail-data-api
Evidence: Page text supplied by user October 23, 2026; page labels itself updated eight months ago.

- AskTreez Retail Data API provides raw reporting data through DOMO as JSON for custom reports.
- Intended users include retailers and some partners. Business Development qualifies the requesting organization.
- Access contact: partners@treez.io. Published instructions say to request a CLIENT ID and CLIENT SECRET. These instructions describe the separate Data API; current authentication and applicability of SellTreez V3 migration require confirmation.
- Data/access support contact: asksupport@treez.io.
- Access is premium and paid; no dollar amount, billing unit, or minimum term appears on this page. Do not apply SellTreez sandbox/Stock/Invoice prices to Retail Data without confirmation.
- The page expects API, SQL/query, and analytics skills. Implementation should accommodate the firm's limited Python experience through documented setup and a simple staff-operated extraction process; the published skill expectations do not demonstrate that Python specifically is mandatory.
- Ticketline, Inventory, and Payment tables update incrementally; other tables daily. last_retrieved_timestamp indicates refresh timing. Treez recommends requesting a day's complete available data the following afternoon. Refresh frequency does not establish historical retention or completeness of returns/corrections.
- Page links to DOMO developer documentation, an API Explorer, and a Postman collection. These may help inspect request structure and schemas, subject to availability; credentials have not been requested.

Access/cost website research status: Published routes and contacts documented. CPA-firm eligibility, current quotes for both services, permissions, contract applicability, and retention remain unresolved for later outreach. Next research topic: V3 authentication, followed by endpoint-specific historical coverage.

## Step 3 — V3 authentication requirements

Source: https://code.treez.io/reference/authentication
Evidence: Page text and examples supplied by user October 23, 2026; page labels itself updated 15 days ago. No keys generated and no authentication tested.

### Documented requirements

- Self-signed PEM X.509 certificate with a 4096-bit RSA public key. Treez recommends OpenSSL; Git for Windows includes an executable. This is a documented option, not proof it is the only Windows installation method.
- Submit only the public .crt to api-support@treez.io. Retain the private .key securely outside Git and shared research material.
- Treez registers the certificate, supplies a Certificate ID, and configures permitted organizations, dispensaries, and endpoints. An Organization ID identifies the target organization.
- Sign each request separately and supply the result in the Authorization header. Documentation specifies a 30,000 millisecond TTL and says other TTL values return HTTP 400.
- Node example fields: aud (request URL), iss (Certificate ID), oid (Organization ID), iat and exp (milliseconds), and recommended jti (unique token ID). RSA-SHA256 signs the encoded JSON object.
- The supplied example command sets a five-year certificate duration and creates an unencrypted private key using -noenc. That is an example configuration, not an established mandatory lifetime or our approved storage design.
- The site offers Python, Node, Java, Ruby, Go, and Postman examples and expressly labels the examples non-production-ready. Only Node and Postman example bodies were supplied in this step.

### Implementation details to verify

- The examples construct two dot-separated components (encoded JSON and signature), rather than the usual three-part JWT serialization. Implement the vendor's verified format; do not assume a standard JWT library's default output will work.
- Node uses URL-safe Base64 while Postman uses ordinary Base64. Confirm accepted encoding and canonical audience URL with the validation endpoint and Treez support if necessary.
- Postman instructions incorrectly illustrate privateKey PEM boundaries as BEGIN/END CERTIFICATE. The private signing key must be a private-key PEM, distinct from the public certificate; verify the accepted key encoding.
- The prose describes public-key decryption; operationally the public key verifies the request signature. Do not treat the request body or token as encrypted by signing.
- Node calls Date.now() separately for iat and exp; capture one timestamp in production so the specified TTL is exact. Maintain accurate system time.
- Examples log signed authorization values and embed private-key material or load executable library text. Production code should avoid credential/token logging and use securely stored keys and controlled dependencies.
- Confirm certificate expiration/rotation/revocation procedures and endpoint permissions. Authentication for the separate DOMO Retail Data API remains unconfirmed.

### Proposed staff experience

A future extractor should handle request signing internally. Staff should select client and date range and run a documented command or launcher; routine use should not require writing Python or generating tokens manually. This is a design goal, not an implemented feature.

Next research topic: Historical coverage, beginning with the close-date ticket endpoint and distinguishing it from last-updated retrieval limits.

## Step 4 — Historical coverage: close-date endpoint

Source: https://code.treez.io/reference/ticket-get-by-close-date
Evidence: Page text and displayed test response supplied by user October 23, 2026.

- GET /dispensary/v3/{dispensary}/ticket/closedate/{date}/page/{page}/pagesize/{pagesize} retrieves tickets closed on a specified date.
- Required path values: dispensary, date (YYYY-MM-DD), page, and pagesize.
- Optional full_decimals requests unrounded dollar amounts where applicable. include_cost requires permission.
- The reviewed page does not state earliest available date, retention period, maximum page size, starting page number, or pagination completion rules. A full-year backfill is therefore not yet confirmed.
- The user-displayed Try It request returned HTTP 401 and contained literal placeholder path values (dispensary, date, page, pagesize), with no Authorization header shown. This is not a successful data extraction or a test of historical retention; the exact authentication failure was not diagnosed.
- The displayed error object is not a ticket response schema. The collapsed 200 response is described only as an object in the supplied text; no successful response fields were supplied.

Next website check: Get by last updated date, to establish its distinct date restrictions. Do not retry live calls until valid authorized access and actual request parameters are available.

## Step 4 continued — Last-updated endpoint

Source: User-supplied V3 Get by last updated date page, October 23, 2026 (linked from the close-date reference).

- GET /dispensary/v3/{dispensary}/ticket/lastUpdated/after/{date}/page/{page}/pagesize/{pagesize}
- Required date is a date-time in ISO 8601 format YYYY-MM-DDThh:mm:ss.sss±hh:mm, including a UTC offset. Required dispensary, page, and pagesize are also listed.
- Optional full_decimals and permission-restricted include_cost are documented.
- The description says tickets closed on the specified date, which conflicts with the lastUpdated/after route and page title. Treat this as an apparent documentation error; exact update selection semantics need confirmation.
- This supplied V3 page does not state a 30-day lookback limit, historical retention, maximum page size, starting page number, or pagination completion rule. Older/general Ticket API documentation previously reviewed states a 30-day restriction for last-updated retrieval; its applicability to current V3 remains unconfirmed. Do not infer either unlimited history or a confirmed V3 30-day limit from this page.
- Displayed HTTP 401 response again used literal placeholder path values and no Authorization header was shown. No authenticated extraction, historical coverage test, or successful response schema was obtained.

Potential future use: capture changed tickets after an extraction checkpoint, subject to verified semantics, pagination stability, and lookback restrictions. Initial full-year extraction remains dependent on verified backfill coverage.

Next website evidence: Ticket API overview/general limitations, followed by a published sample ticket response. Record legacy-versus-V3 applicability explicitly.

## Step 4 continued — Ticket API overview limitations

Source: https://code.treez.io/docs/ticket-apis
Evidence: LIMITATIONS section supplied by user October 23, 2026. Legacy endpoint links remain in this documentation; confirm applicability to current V3.

| Published limitation | Reconciliation implication |
| --- | --- |
| Last-updated retrieval only goes back 30 days; older requests fail | Not an established method for initial full-year backfill. Confirm V3 behavior and keep any future incremental extraction within the verified lookback. |
| Maximum 50 results per request | Retrieve all pages; confirm V3 maximum and completion rules. This is a record count, not a date-range limit. |
| 10 TPS per Treez location | Published rate is 10 transactions/requests per second per location; verify vendor interpretation and V3 applicability, throttle below the ceiling, and handle rate-limit responses. |
| Refunds cannot be handled or processed using Ticket API | Wording concerns refund functionality; it does not establish whether existing refunds are present in GET responses. Historical refund retrieval remains unresolved. |

Other listed limitations concern writing tickets: updates after payment, payment during COMPLETED transition, separate product/payment requests, unsupported partial payments, item-level rather than cart-level discount application, and delivery-zone configuration not enforced by Create Ticket. These are not evidence that existing partial tenders, cart discounts, or returns are absent from read responses.

No full-year close-date retention limit is stated in this supplied section. Full-year retrieval remains unconfirmed. Next research: published Ticket API sample responses to inspect transaction IDs, sales lines, package tags, timestamps, and return representation.
