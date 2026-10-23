# POS API Integration

## Purpose

This repository is the central workspace for researching, documenting, and developing integrations with client point-of-sale (POS) systems. Its purpose is to make client data extraction repeatable, reduce manual report downloads, and provide reliable source data for accounting, reconciliation, and compliance workflows.

The work begins with cannabis retail POS platforms and supports both client-specific implementations and reusable procedures across clients.

## Platforms in Scope

| Platform | Scope |
| --- | --- |
| Treez | API and reporting research, data extraction, and integration development |
| Dutchie | API and reporting research, data extraction, and integration development |
| Cova | API and reporting research, data extraction, and integration development |
| Flowhub Maui | API and reporting research, data extraction, and integration development |
| BioTrackTHC | API and reporting research, data extraction, and integration development |

These platforms represent the current client integration scope. Inclusion does not mean that API access has been obtained or an integration has been built or tested. Additional platforms may be added as client needs develop.

## Objectives

- Identify available APIs, reporting interfaces, export methods, access requirements, and vendor restrictions.
- Document authentication, permissions, available fields, historical coverage, pagination, rate limits, and other extraction constraints.
- Develop repeatable extraction procedures and tools using the methods supported by each platform, including JSON responses and CSV exports where available.
- Preserve transaction detail needed to reconcile sales, returns, discounts, taxes, tenders, inventory, and METRC activity.
- Prepare consistent datasets for Excel, Power Query, Python, and other accounting or reporting tools.
- Support monthly, quarterly, and calendar-year reconciliation, including periods of up to 12 months.
- Record known limitations, validation results, and unresolved questions so staff can reproduce and review the work.

## Repository Contents

As work progresses, this repository will hold:

- Platform research, official documentation references, and vendor questions.
- Access and setup procedures for authorized client integrations.
- Data dictionaries, field mappings, and source-to-output specifications.
- Extraction scripts, configuration examples, and Power Query M code where appropriate.
- Validation procedures, reconciliation controls, and exception-handling guidance.
- Sanitized sample data and implementation notes.

Reusable components should be separated from client-specific configuration so that improvements can be applied across engagements.

## Data Reliability

Each integration should document what was extracted, the reporting period, the applicable location or license, and the extraction method. Validation should address completeness, duplicate records, transaction identifiers, timestamps and time zones, returns and voids, monetary precision, and agreement with available source-system control totals.

Official vendor documentation, observed system behavior, and assumptions should be identified separately. Unverified capabilities and unresolved differences should remain explicit until tested.

## Credentials and Client Data

Do not commit passwords, API keys, access tokens, or unredacted customer, patient, employee, or payment information. Use configuration templates and sanitized examples in the repository. Keep live credentials and client production datasets in approved storage outside Git.

## Initial Work

The initial research focus is Treez integration for Five Lakes Farm. The findings and procedures will establish a repeatable approach for the other POS platforms in scope.
