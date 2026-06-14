# Cloud Autonomy Applicability (BSI C3A)

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

## Decision

- Result: [Applicable / N/A / Open]
- Date:
- Feature / system:
- Owner:
- Evidence location:

## Scope

- Cloud services in scope:
- Service model: [SaaS / PaaS / IaaS / managed service / registry / artifact hosting / other]
- Provider(s):
- Deployment or operational dependency:
- Data classifications involved:

## Applicability Rationale

- Why C3A applies or is N/A:
- Is cloud use part of the released or operated system?
- Is cloud use limited to development infrastructure? If yes, record the
  toolchain rationale for `N/A`.
- Related S-ADR(s):
- Related Zero Trust note:
- Related C5 or assurance evidence:

## Cloud-Service Selection

| Decision factor | Evidence | Status |
| --- | --- | --- |
| Required cloud capability | | [OK / Open / N/A] |
| Business or learning rationale | | [OK / Open / N/A] |
| Alternative providers considered | | [OK / Open / N/A] |
| Selection constraints | | [OK / Open / N/A] |

## Provider Dependencies

| Dependency | Impact | Mitigation / rationale | Status |
| --- | --- | --- | --- |
| Identity / access | | | [OK / Open / N/A] |
| Runtime / hosting | | | [OK / Open / N/A] |
| Data storage / backup | | | [OK / Open / N/A] |
| CI/CD / artifact flow | | | [OK / Open / N/A] |
| Monitoring / logging | | | [OK / Open / N/A] |

## Audit and Assurance Evidence

- Available audit report(s):
- C5 or equivalent evidence:
- Contractual or service documentation:
- Open evidence gaps:

## Autonomy and Lock-In Risks

| Risk | Trigger | Consequence | Mitigation / accepted rationale |
| --- | --- | --- | --- |
| Provider lock-in | | | |
| Data export limitation | | | |
| Configuration portability | | | |
| Operational dependency | | | |
| Jurisdiction / support dependency | | | |

## Exit and Portability

- Export path:
- Restore / migration path:
- Required documentation:
- Re-test trigger:

## Follow-Up Tasks

- [ ] Close open C3A applicability questions.
- [ ] Link this record from the relevant S-ADR or architecture plan.
- [ ] Revisit this record before release or provider change.
