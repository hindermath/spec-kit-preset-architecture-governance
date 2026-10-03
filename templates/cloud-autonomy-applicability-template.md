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
- Linked C5 report type: [Type 1 / Type 2 / Unknown / N/A]
- Linked C5 point-in-time date or audit period:
- Linked C5 operating-effectiveness status and open gaps:

## Kriterienabdeckung / Criteria coverage

- C3A catalogue/version: BSI C3A v1.0 (2026-04-27)
- Catalogue reference and SHA-256: resolve `c3a-criteria-catalog`
- Assessment scope and cloud service(s):
- Provider(s), assessment owner and reviewer:
- C5 foundation evidence and unresolved assurance gaps:

DE: Alle 30 Gruppen bleiben sichtbar. Pro anwendbarem C-/AC-Identifier ist
ein eigener Detailnachweis erforderlich. N/A braucht eine Begruendung; Open
braucht Grund, Owner, Aktion und Wiedervorlage. Anwendbar verlangt Evidence
oder eine ausdrueckliche offene Luecke. Eine leere Zeile ist keine Abnahme.
Die bisherigen Themenabschnitte unten verweisen auf diese Nachweise.

EN: Retain all 30 groups. Record each selected criterion and additional
criterion using the detail fields below. Applicable needs evidence or an
explicit open gap; N/A needs rationale; Open needs reason, owner, action and
reevaluation. Missing groups or unfilled rows cannot mean satisfied or N/A.
The thematic sections below summarize and link this criterion evidence.

| Group | Applicability | Selected exact C / AC IDs | Evidence / details | Result | Rationale / risk / follow-up |
| --- | --- | --- | --- | --- | --- |
| SOV-1-01 | Open | | | Open | |
| SOV-1-02 | Open | | | Open | |
| SOV-1-03 | Open | | | Open | |
| SOV-1-04 | Open | | | Open | |
| SOV-2-01 | Open | | | Open | |
| SOV-2-02 | Open | | | Open | |
| SOV-2-03 | Open | | | Open | |
| SOV-3-01 | Open | | | Open | |
| SOV-3-02 | Open | | | Open | |
| SOV-3-03 | Open | | | Open | |
| SOV-3-04 | Open | | | Open | |
| SOV-3-05 | Open | | | Open | |
| SOV-4-01 | Open | | | Open | |
| SOV-4-02 | Open | | | Open | |
| SOV-4-03 | Open | | | Open | |
| SOV-4-04 | Open | | | Open | |
| SOV-4-05 | Open | | | Open | |
| SOV-4-06 | Open | | | Open | |
| SOV-4-07 | Open | | | Open | |
| SOV-4-08 | Open | | | Open | |
| SOV-4-09 | Open | | | Open | |
| SOV-4-10 | Open | | | Open | |
| SOV-5-01 | Open | | | Open | |
| SOV-5-02 | Open | | | Open | |
| SOV-5-03 | Open | | | Open | |
| SOV-5-04 | Open | | | Open | |
| SOV-5-05 | Open | | | Open | |
| SOV-6-01 | Open | | | Open | |
| SOV-6-02 | Open | | | Open | |
| SOV-6-03 | Open | | | Open | |

### Detailnachweis je Identifier / Detail record per identifier

- Exact identifier (for example SOV-3-01-C3), name and catalogue page:
- Kind: [Criterion / Additional Criterion]
- Selected variant(s) and selection rationale:
- Applicability: [Applicable / N/A / Open]
- Evidence reference, revision/date and provenance:
- Evidence origin: [Provider claim / Provider report / Customer evidence / Independent review]
- Customer-side responsibilities and review scope:
- Result: [OK / Open / N/A]
- Rationale, exceptions and residual risk:
- Gap reason, follow-up owner, action and due condition / reevaluation trigger:
- Related SI references and interpretation (not an independently satisfied control):
- Supporting C5 reference, report type and assurance limits:

DE: Varianten werden anhand des gebundenen BSI-Katalogs gewaehlt, nicht aus
Standort oder Marketing abgeleitet. C1/C2 sind nicht pauschal Reifegradstufen;
mehrere Varianten koennen je Scope relevant sein. AC wird bewusst ausgewaehlt
oder begruendet nicht angewendet. SOV-4-01-C3 ist im Original trotz des
C3-Suffixes ein Additional Criterion. SI erklaert Kriterien und ist kein
separater Kontrollnachweis. SOV-7/SOV-8 gehoeren nicht zu diesem C3A-Katalog.

EN: Consult the pinned catalogue for exact variant requirements. Never infer
the stricter variant or a generic compliance result. Keep selected C/AC IDs
distinct; SI informs interpretation rather than creating another passed
control. C3A assumes a C5 security foundation, but a linked C5 report does not
automatically satisfy C3A criteria. Record unavailable evidence as Open.
This framework neither certifies C3A nor performs a provider audit.

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
