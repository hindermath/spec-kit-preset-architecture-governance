# Security Quality Attribute Scenarios (iSAQB CPSA-F)

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
