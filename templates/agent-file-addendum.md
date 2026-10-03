## Architecture Governance Agent Guidance

- Identify trust boundaries and changed data flows before recommending an
  implementation. Name the boundary, the direction of data flow, and the
  data classification.
- For every architecturally significant decision, create or update a
  Security Architecture Decision Record (S-ADR) using `adr-template`.
  Do not bury such decisions in implementation tasks.
- Treat MSL feasibility as an architectural runtime constraint when
  platform or runtime choices are involved. Reference the architectural
  reason; do not duplicate code-level secure-coding rules.
- For threat modelling, use `STRIDE`+`CIA` as the base. Add `CAPEC`
  patterns for the highest-risk paths. Each threat must have a
  mitigation, an accepted-risk note, or a deferral with re-evaluation
  trigger.
- For arc42 Section 8 security cross-cutting concepts, surface gaps in
  authentication, authorisation, encryption in transit/at rest, input
  validation, error handling, logging, dependencies, or deployment.
- Evaluate `Zero Trust` (NIST SP 800-207) applicability for distributed,
  service-based, cloud-near, or remotely managed systems.
- For long-lived projects, surface `OWASP SAMM` follow-up actions when
  the maturity posture is touched.
- Evaluate `BSI C3A` cloud autonomy applicability when the project selects,
  operates, or materially depends on cloud services. Record `Applicable`,
  `N/A`, or `Open` and identify cloud-service selection, provider
  dependencies, audit evidence, autonomy risks, and exit/portability
  concerns where applicable.
- Evaluate `BSI C5` cloud compliance assurance when cloud assurance, C5
  testat/report status, shared-responsibility gaps, provider/subprocessor
  dependencies, data location, logging, backup, or incident evidence are in
  scope. Record `Applicable`, `N/A`, or `Open`.
- Surface required architecture evidence under `docs/security/` (S-ADRs
  in `docs/security/adr/`).
- Document every `N/A` decision with rationale; never silently omit.
- Model multi-repository remote delivery as a resumable transaction. Record
  stable identifiers, exact heads, completed operations, and revalidation
  boundaries instead of assuming one process owns the whole transaction.
- Keep post-merge actions manifest-declared and idempotent. Worker or component
  handoffs may report outcomes but must not introduce executable closeout
  commands.
- Revalidate remaining direct and stacked dependencies after every structural
  change, including merge, rebase, base deletion, or default-branch movement.

## Audit-Ready Spec-Kit Evidence

- When this preset applies, generated or updated Markdown evidence must include the Spec-Kit run, owner/reviewer, evidence path, applicability decision, N/A rationale where relevant, and open follow-up tracking.
- Do not treat an unfilled starter template as evidence. Evidence exists only after the current run has recorded concrete decisions, paths, and rationale.

## C3A-/C5-Evidence-Vertrag / C3A/C5 evidence contract

DE: Bei anwendbarem C3A alle 30 Gruppen aus `c3a-criteria-catalog` v1.0
sichtbar halten; je ausgewaehltem C-/AC-Identifier Evidence und Variante mit
Begruendung erfassen. SI ist Erlaeuterung, kein bestandener Kontrollpunkt.
N/A braucht Begruendung; Open braucht Grund, Owner, Aktion und Wiedervorlage.
Providerbehauptungen von unabhaengiger Pruefung und Kundenpflichten trennen.
C5 Typ 1 ist zeitpunktbezogen und kein Wirksamkeitsnachweis ueber einen
Zeitraum. Typ 2 braucht Pruefzeitraum und Wirksamkeitsbewertung; Unknown bleibt
eine offene Luecke. C5 erfuellt C3A nicht automatisch. Keine Evidence erfinden,
kein Audit oder Zertifikat behaupten und historische Nachweise nicht umschreiben.

EN: For applicable C3A, retain all 30 groups from `c3a-criteria-catalog` v1.0;
record exact selected C/AC IDs, variant rationale and attributable evidence.
SI informs interpretation, not another passed control. N/A requires rationale;
Open requires reason, owner, action and reevaluation. Distinguish provider
claims, independent review and customer responsibilities. C5 Type 1 is
point-in-time assurance, not sustained operating effectiveness. Type 2 requires
audit period and effectiveness assessment; Unknown remains an open gap.
C5 does not automatically satisfy C3A. Do not fabricate evidence, claim an
audit/certification or rewrite historical records.

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
