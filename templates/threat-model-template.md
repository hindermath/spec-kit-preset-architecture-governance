# Threat Model

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

## Scope

- System or feature:
- Owner:
- Date:
- Reviewers:
- Related S-ADRs:

## Architecture Snapshot

- Components in scope:
- External actors and systems:
- Data classifications handled (public, internal, confidential,
  restricted):

## Trust Boundaries

| ID | Boundary | Crossing direction | Data classification | Validation point |
|----|----------|--------------------|---------------------|------------------|
| TB-1 | | | | |
| TB-2 | | | | |

## STRIDE × CIA Matrix

For each STRIDE category, list the identified threats and mark the CIA
impact (C / I / A — one or more) and a coarse risk score (Low /
Medium / High / Critical).

| ID | STRIDE category | Threat | C | I | A | Risk |
|----|-----------------|--------|---|---|---|------|
| T-1 | Spoofing | | | | | |
| T-2 | Tampering | | | | | |
| T-3 | Repudiation | | | | | |
| T-4 | Information disclosure | | | | | |
| T-5 | Denial of service | | | | | |
| T-6 | Elevation of privilege | | | | | |

## CAPEC References

For the highest-risk threats, reference the matching `CAPEC` attack
patterns and note any pattern-specific mitigations.

| Threat ID | CAPEC ID(s) | Pattern name | Notes |
|-----------|-------------|--------------|-------|
| | | | |

## Mitigations

| Threat ID | Mitigation / accepted risk / deferral | Owner | Re-evaluation trigger |
|-----------|---------------------------------------|-------|-----------------------|
| | | | |

## Cross-References

- Related ADRs / S-ADRs:
- arc42 Section 8 sections affected:
- ASVS controls and Level (if web/API):
- Supply-chain evidence entries (if dependencies are part of the threat
  surface):

## Follow-Up

- Open threats:
- Required architectural changes:
- Next threat-model review trigger:

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
