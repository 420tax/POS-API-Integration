# Project Manifesto

## Purpose

Build dependable POS data integrations that James Campbell and his staff can operate as part of their accounting work. The project should reduce manual downloads and repetitive preparation while preserving the detail and controls needed for reconciliation and professional review.

The current scope includes Treez, Dutchie, Cova, Flowhub Maui, and BioTrackTHC. Treez for Five Lakes Farm is the initial implementation.

## Design for the People Who Will Use It

James is a CPA with accounting, reconciliation, and Power Query experience. He does not have Python programming skills. Staff knowledge will vary, and Python proficiency must not be assumed or required for routine use.

These are design requirements. A successful implementation must let users obtain reliable results without writing code, editing scripts, managing Python packages, or diagnosing programming errors.

James and staff will define accounting requirements, explain source-system behavior, review exceptions, and validate results. Technical development should translate those requirements into a maintained process with clear operating instructions.

## Keep the Operating Process Simple

The intended workflow is:

1. Select the client, location or license, and date range.
2. Supply downloaded source files or use an authorized connection, depending on the integration.
3. Run the process through a documented shortcut, launcher, or simple interface.
4. Receive prepared data, a control report, and any exceptions requiring attention.
5. Refresh the accounting workbook and review the results.

Routine operation should not require a code editor or knowledge of command-line syntax. Setup, credential renewal, and maintenance must have their own documented procedures. If technical support is required, staff should know what information to provide and how to obtain help.

## Give Each Tool a Clear Job

| Component | Intended responsibility |
| --- | --- |
| Python, where suitable | Retrieve data, handle API pagination, prepare fields, and produce consistent output files and run reports. |
| Power Query | Import prepared data and apply documented workbook transformations and reconciliation logic. |
| Excel | Present control totals, exceptions, supporting detail, and review conclusions. |

Python is a candidate implementation tool. Final choices should follow verified vendor capabilities and the practical needs of the workflow. Any movement of reconciliation logic between tools must be documented so users can trace how results were calculated.

## Validate Before Automating Further

Begin with available exports when they are sufficient to build and test the data preparation process. Add API retrieval after access, field coverage, and extraction behavior have been verified.

An API connection is useful only if the resulting data is complete and suitable for the intended reconciliation. Automation must preserve the transaction detail needed to explain differences, including separate sales that share a timestamp and package tag.

## Make Every Run Reviewable

Each run should provide:

- The client, location or license, requested period, and actual data coverage.
- The extraction time, source method, and tool version.
- Source and output record counts, relevant financial totals, and validation results.
- Clear treatment of returns, voids, discounts, taxes, duplicate records, timestamps, and monetary precision.
- An exception report identifying missing information, failed checks, or unresolved differences.
- A clear completion status that distinguishes successful, incomplete, and failed runs.

Retain original source files or responses in approved client storage and keep a traceable relationship between those sources and prepared outputs. Repeated runs should avoid accidental duplication or silent overwriting of prior evidence.

## Explain Problems in Plain Language

Error messages should explain what failed, whether any output is usable, and the next action. Staff should not have to interpret a Python traceback to decide whether a reconciliation can proceed.

Technical diagnostic details should be available for support without exposing credentials or unnecessary personal information. Incomplete downloads and failed validation must be visible; they must not appear to be successful, complete results.

## Build Once, Reuse Carefully

Use common procedures and output conventions across platforms where the underlying data supports them. Keep platform differences and client configuration explicit. Reuse should simplify work without concealing differences in definitions, available fields, or reporting behavior.

Support monthly, quarterly, and calendar-year work, including periods of up to 12 months, subject to verified source-system limits. Document any required batching or historical access restrictions.

## Document and Maintain the Process

Every usable integration needs setup instructions, a short operating guide, sample outputs, known limitations, and recovery steps. Changes to vendor APIs, source reports, or output formats must be assessed before they affect established workbooks.

Keep credentials and production client datasets outside Git. Use configuration templates and sanitized examples in the repository. Document required access and credential handling without recording secret values.

AI assistance may support development and troubleshooting. Routine operation must remain documented and reproducible without depending on the memory of a particular chat.

## Definition of Success

An integration is ready for routine use when a staff member can follow its instructions, run it without editing code, recognize whether it completed successfully, locate the output, reconcile the control totals, and identify exceptions requiring review or support.

James retains responsibility for accounting judgments and approval of the results. The software must make those judgments easier to exercise by providing dependable data and visible evidence.

If a normal reconciliation requires James or his staff to open a code editor and repair Python scripts, the implementation has not met this manifesto's usability requirements.
