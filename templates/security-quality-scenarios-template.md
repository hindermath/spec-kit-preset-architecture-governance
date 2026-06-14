# Security Quality Attribute Scenarios (iSAQB CPSA-F)

## Spec-Kit Run Evidence

- Feature / Spec ID:
- Spec-Kit phase: [specify / plan / tasks / implement / review / release]
- Branch / commit / PR:
- Run date:
- Evidence owner:
- Reviewer:
- Standards / criteria checked: ISO 27001/27002 secure architecture controls, STRIDE, CAPEC, arc42, iSAQB CPSA-F, NIST Zero Trust, OWASP SAMM, BSI C3A, BSI C5
- Decision: [Applicable / N/A / Open]
- Evidence path:
- N/A rationale, if not applicable:
- Open follow-up owner and trigger:
- Re-evaluation trigger:
- Certification-readiness note: Use this record as architecture and cloud-assurance evidence; C5 evidence must link actual reports/testats where available and record customer-side review responsibility.

## Audit Evidence Matrix

| Checkpoint / control reference | Applicability | Evidence produced or linked | Result | Residual risk / rationale |
| --- | --- | --- | --- | --- |
| Spec-Kit run scope is identified | [Applicable / N/A / Open] | | [OK / Open / N/A] | |
| Standard-specific criteria are mapped | [Applicable / N/A / Open] | | [OK / Open / N/A] | |
| Evidence artefact path is recorded | [Applicable / N/A / Open] | | [OK / Open / N/A] | |
| N/A decisions are justified | [Applicable / N/A / Open] | | [OK / Open / N/A] | |
| Open findings have owner and trigger | [Applicable / N/A / Open] | | [OK / Open / N/A] | |

## Context

- System or feature:
- Owner:
- Date:
- Related S-ADRs and threat-model entries:

## How to Use

For each security-relevant quality attribute (confidentiality, integrity,
availability, authenticity, non-repudiation, accountability), describe one
or more concrete scenarios using the iSAQB CPSA-F structure:

- **Source**: who or what triggers the stimulus
- **Stimulus**: the event the system must react to
- **Artefact**: the part of the system stimulated
- **Environment**: under which operating conditions
- **Response**: what the system does
- **Response Measure**: a measurable success criterion (latency,
  probability, threshold, count)

## Scenario Template

### Scenario S-NN — short title

- Quality attribute (C / I / A / Authenticity / Non-repudiation /
  Accountability):
- Source:
- Stimulus:
- Artefact:
- Environment:
- Response:
- Response Measure:
- Verification approach (test, audit, monitoring):
- Verification evidence location:

## Suggested Coverage

- At least one Confidentiality scenario for any feature touching personal
  or restricted data
- At least one Integrity scenario for any feature handling financial,
  configuration, or audit data
- At least one Availability scenario for any feature on a critical user
  flow
- At least one Authentication or Non-repudiation scenario for any
  feature handling identity or signed actions

## Follow-Up

- Open quality scenarios:
- Required architectural changes:
- Re-evaluation trigger:
