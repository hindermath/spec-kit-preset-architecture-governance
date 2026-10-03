## Architecture Governance Applicability

- Identify whether runtime, hardware, or platform constraints affect
  memory-safe language choice and which architectural reason applies.
- Identify trust boundaries created, removed, or changed by this feature.
- Identify the data flows that cross trust boundaries and the data
  classifications involved (public, internal, confidential, restricted).
- Identify whether a `STRIDE`+`CIA` threat model entry must be added or
  updated; reference relevant `CAPEC` patterns for high-risk paths.
- Identify whether a Security Architecture Decision Record (S-ADR) must
  be created or revised — see `adr-template`.
- Identify whether the `arc42` Section 8 security cross-cutting concepts
  document needs an update (auth, authorisation, encryption in transit
  and at rest, input validation, error handling, logging, dependencies,
  deployment security).
- Identify whether security quality attribute scenarios (iSAQB CPSA-F)
  apply to this feature.
- Identify whether `Zero Trust` (NIST SP 800-207) applicability must be
  reviewed for new or changed distributed, service-based, or
  remote-access flows.
- Identify whether the `OWASP SAMM` improvement plan is affected.
- Identify whether `BSI C3A` cloud autonomy applicability must be reviewed
  for cloud-service selection, SaaS/PaaS/IaaS, managed services,
  container/artifact hosting, or provider-dependent deployments.
- Identify whether `BSI C5` cloud compliance assurance must be reviewed for
  cloud-service selection, SaaS/PaaS/IaaS, managed services,
  container/artifact hosting, provider-dependent deployments, or cloud
  assurance reviews.
- Record any justified `N/A` decisions with rationale. Silent omission is
  not allowed.

## Audit Evidence Applicability

- Record whether this Spec-Kit run requires an evidence document or checklist update.
- Use `Applicable`, `N/A`, or `Open` for each relevant standard or governance checkpoint.
- Document every `N/A` decision with a short rationale and re-evaluation trigger.
- Link the planned evidence path from the feature spec; silent omission is not allowed.

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
