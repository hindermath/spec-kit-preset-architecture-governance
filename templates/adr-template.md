# Security Architecture Decision Record (S-ADR)

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

## ID and Title

- ID: S-ADR-NNN
- Title:
- Status: (proposed / accepted / superseded by S-ADR-NNN / deprecated)
- Date:
- Author(s):

## Context

What architectural problem is being solved? Which trust boundaries,
data flows, regulatory requirements, or runtime constraints frame the
decision?

## Decision

State the architectural decision in the active voice: "We will …".

## Security and Architecture Implications

How does this decision interact with the architectural security
principles?

- Trust boundaries:
- Defense in depth:
- Least privilege:
- Fail-safe defaults:
- Attack surface reduction:
- Separation of concerns:
- Secure configuration / secret handling:
- Supply-chain implications:

## Alternatives Considered

For each alternative: option, security trade-offs, reason for rejection.

## Compliance Evidence

| Standard / framework | Applies? | Reference / control IDs | Evidence location |
|----------------------|----------|-------------------------|-------------------|
| `NIST SSDF` (SP 800-218) | | | |
| `CWE Top 25` | | | |
| `OWASP ASVS` (Level 1/2/3) | | | |
| `SBOM` / `VEX` / `SLSA` | | | |
| `OWASP SAMM` | | | |
| `Zero Trust` (NIST SP 800-207) | | | |
| `EU CRA` (Reg. 2024/2847) | | | |
| ISO 27001/27002 (A.8.27 / A.8.28) | | | |
| Other (name) | | | |

## Consequences

- Positive:
- Negative / accepted trade-offs:
- Required follow-up work:
- Re-evaluation trigger (date, scope change, incident):

## Cross-References

- Related ADRs / S-ADRs:
- Threat model entries:
- arc42 Section 8 sections affected:

## Datenschutz und regulatorische Architektur / Privacy and regulatory architecture

DE: Die projektspezifische Anwendbarkeit von DS-GVO, KI-VO, CRA, NIS2 und
DORA wird durch Security-Evidence gefuehrt; hier keine zweite Rechtsentscheidung
erfinden. Bei installiertem Security-Preset dessen Detailvorlagen nutzen,
sonst gleichwertige projektgefuehrte Nachweise verlinken. Beispielprogramm,
Entwicklungswerkzeuge und Organisation getrennt betrachten; AI-SBOM: N/A
und Ausbildungszweck sind keine allgemeine regulatorische Ausnahme.
Privacy by Design/Default: Datenminimierung, Zweck, Empfaenger, Regionen,
Speicherbegrenzung, Loeschung und Betroffenenrechte in Datenfluessen abbilden.
KI-Tool-/Produktgrenzen, Prompt-, Logging- und Telemetriepfade pruefen.
NIS2-/DORA-relevante Dienstleisterabhaengigkeit, getestete Wiederherstellung,
Verfuegbarkeit, Konzentrationsrisiko und Exit-Faehigkeit rollenbezogen planen.
C3A/C5-Nachweise ersetzen keinen Datenschutz-, NIS2- oder DORA-Nachweis.
EN: Project Security evidence owns GDPR, AI Act, CRA, NIS2 and DORA
applicability; do not create a competing legal decision. Use Security detail
templates when installed, otherwise equivalent project-owned records.
Assess sample product, development tools and organisation separately;
AI-SBOM: N/A and education are not blanket regulatory exemptions.
Map privacy by design/default, minimisation, purpose, recipients, regions,
retention, deletion and subject rights to data flows. Review AI/tool boundaries
and prompt/log/telemetry paths. Plan role-specific supplier dependencies,
tested recovery, availability, concentration risk and exit capability for
NIS2/DORA-related scope. C3A/C5 evidence does not replace regulatory evidence.

- Applicability record / exact scope / owner / review date:
- Personal-data inventory / synthetic-data decision:
- Data flow / purpose / trust boundary / receiver / region:
- Retention / deletion / defaults / subject-rights interface:
- AI/tool usage boundary / prompt and logging safeguards:
- Supplier dependency / tested recovery / exit / concentration risk:
- Legal Open finding / qualified reviewer / next action / due date:
