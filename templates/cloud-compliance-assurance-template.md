# Cloud Compliance Assurance (BSI C5)

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
- Jurisdictions / regions involved:

## Applicability Rationale

- Why BSI C5 applies or is N/A:
- Is cloud use part of the released or operated system?
- Is cloud use limited to development infrastructure? If yes, record the
  toolchain rationale for `N/A`.
- Related C3A cloud-autonomy record:
- Related Zero Trust note:
- Related S-ADR(s):

## Cloud-Service Selection

| Decision factor | Evidence | Status |
| --- | --- | --- |
| Required cloud capability | | [OK / Open / N/A] |
| Business or learning rationale | | [OK / Open / N/A] |
| Alternatives considered | | [OK / Open / N/A] |
| Security and compliance constraints | | [OK / Open / N/A] |

## C5 Audit / Assurance Status

- C5 attestation or report available: [Yes / No / N/A / Open]
- C5 report type: [Type 1 / Type 2 / Unknown / N/A]
- Report date:
- C5 criteria/version:
- Point-in-time assessment date (Type 1):
- Audit period start (Type 2):
- Audit period end (Type 2):
- Operating effectiveness assessed over a period (Type 2 only): [Yes / No / N/A / Open]
- Exceptions / deviations:
- Customer-side controls / responsibilities:
- Report / evidence reference:
- Open assurance gaps / follow-up (owner, action, due condition or trigger):
- Covered provider / service:
- Covered region(s):
- Covered control scope:
- Report validity / renewal date:
- Equivalent assurance evidence, if no C5 report exists:

### Berichtstyp und Grenzen / Report type and limits

DE: Typ 1 beschreibt Design, Beschreibung und Implementierung der Kontrollen
am Bewertungsstichtag; er belegt keine
Wirksamkeit ueber einen Pruefzeitraum. Typ 2 benoetigt Beginn, Ende und die
belegte Bewertung der operativen Wirksamkeit. Ist der Typ unbekannt, bleibt
er Unknown mit Open-Folgearbeit. Fehlende Typ-2-Evidence fuer eine benoetigte
Zeitraumaussage bleibt eine offene Luecke. Report-Verfuegbarkeit, Scope,
Ausnahmen und kundenseitige Verantwortung sind getrennt zu bewerten.

EN: Type 1 concerns control description, design and implementation as of a
point in time and cannot establish sustained operating
effectiveness. Type 2 requires an audit period and evidence that operating
effectiveness was assessed. Unknown stays Unknown with an Open follow-up.
Never infer report type or effectiveness from availability or provider claims.
Missing period evidence remains an assurance gap when period assurance is
required. This preset records evidence; it performs no C5 audit or certification.

DE: Bei Typ 1 ist die Zeitraum-Wirksamkeit No oder N/A, niemals Yes aus diesem
Bericht. Bei Typ 2 bleibt ein fehlender Zeitraum oder Wirksamkeitsnachweis
Open; ein Typ-2-Titel alleine rechtfertigt kein OK.

EN: For Type 1, period effectiveness is No or N/A, never Yes based on that
report. For Type 2, missing period/effectiveness evidence remains Open; the
report title alone cannot justify OK.

## Shared Responsibility

| Responsibility area | Provider responsibility | Project responsibility | Gap / mitigation | Status |
| --- | --- | --- | --- | --- |
| Identity and access | | | | [OK / Open / N/A] |
| Network and perimeter controls | | | | [OK / Open / N/A] |
| Data protection and encryption | | | | [OK / Open / N/A] |
| Logging and monitoring | | | | [OK / Open / N/A] |
| Backup and restore | | | | [OK / Open / N/A] |
| Incident response | | | | [OK / Open / N/A] |
| Change and configuration management | | | | [OK / Open / N/A] |

## Provider and Subprocessor Dependencies

| Dependency | Role | Data / access involved | Evidence | Status |
| --- | --- | --- | --- | --- |
| Primary provider | | | | [OK / Open / N/A] |
| Identity provider | | | | [OK / Open / N/A] |
| Hosting / runtime | | | | [OK / Open / N/A] |
| Storage / backup | | | | [OK / Open / N/A] |
| Monitoring / logging | | | | [OK / Open / N/A] |
| Subprocessor(s) | | | | [OK / Open / N/A] |

## Operational Evidence

- Data location evidence:
- Logging / audit evidence:
- Backup / restore evidence:
- Incident notification and response evidence:
- Access review evidence:
- Open evidence gaps:

## Follow-Up Tasks

- [ ] Close open C5 applicability questions.
- [ ] Link this record from the relevant C3A record, S-ADR, or architecture plan.
- [ ] Revisit this record before release, provider change, or material cloud-scope change.
