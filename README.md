# Architecture Governance Preset

Version: `0.6.1`
Status: release candidate; publication pending professional review and CI
Priority: `20`
Requires: Spec-Kit `>=0.8.0` (uses the `wrap` and `append` composition
strategies introduced in `0.8.x`).

## Zweck / Purpose

Dieses Standard-Preset bringt sichere Softwarearchitektur, Threat Modeling,
Zero Trust, Security Architecture Decision Records und Cloud-Assurance-Fragen
in Spec-Kit-Workflows. Es ergänzt `security-governance`, ohne dessen
code- und SDLC-nahe Regeln zu verdoppeln.

*This standard preset injects secure software architecture, threat modeling,
Zero Trust, Security Architecture Decision Records, and cloud-assurance
questions into Spec-Kit workflows. It complements `security-governance`
without duplicating its code-level and SDLC-level rules.*

Das Qualitätsziel ist eine prüffähige Architekturbegründung: Trust
Boundaries, Angriffsflächen, Sicherheitsqualitätsziele, Cloud-Abhängigkeiten,
S-ADRs und begründete `N/A`-Entscheidungen sollen vor der Implementierung
sichtbar sein.

*The quality goal is reviewable architecture reasoning: trust boundaries,
attack surfaces, security quality goals, cloud dependencies, S-ADRs, and
justified N/A decisions should be visible before implementation.*

## Zielgruppen / Audience

Dieses Preset eignet sich, wenn:

- ein System explizite Trust Boundaries oder externe Integrationen besitzt;
- Threat Models und S-ADRs als echte Arbeitsprodukte gepflegt werden sollen;
- Cloud-Auswahl, Provider-Abhängigkeit, Datenort, Audit-Evidence oder Exit
  Risk entscheidungsrelevant sind;
- Security-Architektur getrennt von allgemeiner iSAQB/arc42-Architektur
  geführt werden soll.

*Use this preset for systems with explicit trust boundaries or external
integrations, for teams maintaining threat models and S-ADRs, for cloud
decisions with provider, data-location, audit, or exit-risk relevance, and
when secure architecture should remain separate from general iSAQB/arc42
architecture governance.*

## Lieferumfang / What It Provides

- Addenda für Constitution, Spec, Plan, Tasks und Agent-Guidance
- Wrapper für `speckit.specify`, `speckit.plan` und `speckit.tasks`
- Vorlagen für Threat Models, S-ADRs, arc42 Section 8, Security Quality
  Scenarios, Zero Trust, OWASP SAMM, BSI C3A und BSI C5
- auditfähige Spec-Kit-Run-Evidence-Felder für Anwendbarkeit,
  `N/A`-Begründung, Reviewer, Evidence-Pfad, Restrisiko und Follow-up

*The preset provides addenda for the main Spec-Kit artifacts and agent
guidance, wraps the normal Specify/Plan/Tasks flow, and supplies templates for
threat models, S-ADRs, arc42 Section 8, security quality scenarios, Zero
Trust, OWASP SAMM, BSI C3A, and BSI C5.*

## Nicht enthalten / What It Does Not Provide

Das Preset erstellt kein Threat Model automatisch, bewertet keine Cloud
rechtsverbindlich, validiert keine C5-Testate und führt keine Remote-Prüfungen
aus. Es entscheidet keine Architektur und erteilt keine Repository-, Merge-,
Bypass-, Deployment-, Secret- oder Provider-Administrationsrechte.

*The preset does not create a threat model automatically, does not make legal
cloud decisions, does not validate C5 reports, and does not run remote checks.
It does not decide architecture and grants no repository, merge, bypass,
deployment, secret, or provider-administration authority.*

## Voraussetzungen / Prerequisites

1. kompatible GitHub Spec-Kit CLI;
2. gültige Spec-Kit-Integration im Ziel-Repository;
3. versionierte Constitution und Agent-Guidance;
4. geklärte Evidence-Orte, standardmäßig `docs/security/` und
   `docs/security/adr/`;
5. ein initiales Verständnis von Systemgrenzen, Akteuren, Integrationen und
   Cloud-/Betriebsmodell.

*Before installation, use a compatible GitHub Spec-Kit CLI, a valid Spec-Kit
integration, versioned constitution and agent guidance, clear evidence
locations, and an initial understanding of system boundaries, actors,
integrations, and operating model.*

## Installation / Installation

### Veröffentlichter Tag / Published Tag

Das folgende Beispiel verwendet den bisherigen veroeffentlichten Stand v0.6.0.
Der v0.6.1-Kandidat wird bis zur verifizierten Veroeffentlichung ueber den
Entwicklungs-Checkout geprueft.
*This example uses published v0.6.0. Validate the v0.6.1 candidate using the
development checkout until its release has been verified.*

```bash
specify preset add \
  --from https://github.com/hindermath/spec-kit-preset-architecture-governance/archive/refs/tags/v0.6.0.zip \
  --priority 20
specify preset info architecture-governance
```

### Entwicklungs-Checkout / Development Checkout

```bash
specify preset add --dev /path/to/architecture-governance --priority 20
specify preset info architecture-governance
```

### Empfohlene Kombination / Recommended Composition

| Priority | Preset |
|---:|---|
| 10 | `security-governance` |
| 20 | `architecture-governance` |
| 30 | `isaqb-architecture-governance` |
| 40 | `a11y-governance` |
| 50 | `cross-platform-governance` |
| 60 | `agent-parity-governance` |

`architecture-governance` behandelt sichere Architektur.
`isaqb-architecture-governance` behandelt allgemeine Softwarearchitektur. Wenn
beides relevant ist, werden beide Presets zusammen genutzt.

*`architecture-governance` covers secure architecture.
`isaqb-architecture-governance` covers general software architecture. Use both
presets when both concerns are relevant.*

## Quellkapitel / Source Chapters

- `XI. Memory-Safe Languages (MSL) Preference for Level-2 Projects` as a
  runtime-constraint input
- `XIII. Secure Software Architecture`
- architecture-related applicability rules from `XIV`
- `XVII. Threat Modeling & Attack Pattern Coverage`
- `XVIII. Zero Trust Applicability & Security Program Maturity`

## Standards und Konzepte / Standards and Concepts

- `MSL-aware runtime choice`
- `Trust Boundaries`, `Defense in Depth`, `Least Privilege`,
  `Fail-Safe Defaults`, `Attack Surface Reduction`,
  `Separation of Concerns`, `Secure Configuration`, `Supply-Chain Security`
- `STRIDE` + `CIA` threat modeling with `CAPEC` references
- `arc42` Section 8 security cross-cutting concepts
- Security Architecture Decision Records (`S-ADRs`)
- `iSAQB CPSA-F` security quality attribute scenarios
- `Zero Trust` (NIST SP 800-207)
- `OWASP SAMM`
- `BSI C3A` as conditional cloud sovereignty and autonomy check
- `BSI C5` as conditional cloud compliance and assurance check

## Preset-Strategie / Preset Strategy

- Architektur-Governance an `constitution-template`, `spec-template`,
  `plan-template` und `tasks-template` anhängen
- ein eigenständiges Agent-Guidance-Addendum bereitstellen
- `speckit.specify`, `speckit.plan` und `speckit.tasks` mit einem
  Architektur-Workflow umhüllen
- Starter-Templates für Threat Models, S-ADRs, arc42 Section 8, Quality
  Scenarios, Zero Trust, SAMM, C3A und C5 liefern

## Evidenzvorlagen / Evidence Templates

- `threat-model-template`
- `adr-template`
- `arc42-security-template`
- `security-quality-scenarios-template`
- `zero-trust-applicability-template`
- `samm-assessment-template`
- `cloud-autonomy-applicability-template`
- `cloud-compliance-assurance-template`
- `c3a-criteria-catalog` (BSI v1.0, 30 groups, source hash)

Default evidence location: `docs/security/`. S-ADRs default to
`docs/security/adr/` as one file per decision.

## Prüfung / Verification

```bash
specify preset list
specify preset info architecture-governance
specify preset resolve
specify check
```

Prüfe zusätzlich, ob Security-Architektur-Evidence entweder vorhanden oder im
Plan als zu erzeugendes Artefakt benannt ist.

*Also verify that secure-architecture evidence already exists or is named in
the plan as work to create.*

## Fehlersuche / Troubleshooting

### Threat Modeling wird übersprungen / Threat Modeling Is Skipped

Prüfe, ob Trust Boundaries, externe Schnittstellen oder missbrauchbare Pfade im
Spec oder Plan ausdrücklich benannt sind. Ohne Systemgrenze kann kein gutes
Threat Model entstehen.

*Check whether trust boundaries, external interfaces, or abusable paths are
explicitly named in the spec or plan. Without a system boundary, a useful
threat model cannot emerge.*

### C3A oder C5 ist nicht relevant / C3A or C5 Is Not Relevant

Dokumentiere `N/A` mit kurzer Begründung. Entwicklungsinfrastruktur allein ist
nicht automatisch ein released oder operated cloud runtime.

*Document `N/A` with a short rationale. Development infrastructure alone is
not automatically a released or operated cloud runtime.*

### Allgemeine Architektur fehlt / General Architecture Is Missing

Nutze zusätzlich `isaqb-architecture-governance`, wenn Ziele, Kontext,
Bausteine, Runtime View, Deployment View, ADRs, Risiken oder technische
Schulden dokumentiert werden müssen.

*Also use `isaqb-architecture-governance` when goals, context, building
blocks, runtime view, deployment view, ADRs, risks, or technical debt must be
documented.*

## Version 0.6.0 / Version 0.6.0

C5 Typ 1 beschreibt den bewerteten Zeitpunkt, nicht die Wirksamkeit ueber einen
Zeitraum. Typ 2 braucht Pruefzeitraum und Wirksamkeitsbewertung. Unbekannte
Reporttypen bleiben `Unknown` mit offener Evidence-Luecke. Kriterienversion,
Scope, Ausnahmen und Kundenverantwortung werden getrennt erfasst.

*C5 Type 1 is point-in-time assurance, not sustained operating effectiveness.
Type 2 needs the audit period and effectiveness assessment. Unknown types
remain Unknown with a tracked gap. Record report version, scope, exceptions
and customer-side responsibilities separately.*

C3A erhaelt alle 30 Gruppen aus dem BSI-Katalog v1.0 mit exakten C-/AC-/SI-
Kennungen. Die Themenabschnitte bleiben Einstiegspunkte; sie ersetzen keine
kriterienbezogene Evidence. Jede Gruppe bleibt sichtbar, auch bei `N/A` oder
`Open`. Ein C5-Bericht erfuellt nicht automatisch C3A-Kriterien.

*C3A now includes all 30 groups and exact C/AC/SI identifiers from BSI v1.0.
The thematic summaries link to criterion-level evidence rather than replacing
it. N/A requires rationale; Open requires owner, action and reevaluation.
C5 assurance is not automatic C3A satisfaction. The preset performs no audit.*

Bestehende Evidence bleibt historisch unveraendert. Bei neuer oder wesentlich
geaenderter Cloud-Bewertung wird ein neuer, verlinkter Nachweis erstellt;
fehlende neue Felder sind offene Luecken, kein nachtraegliches Bestehen.
Fuer reine Ausbildungs-/Entwicklungsinfrastruktur ist weiterhin begruendetes
`N/A` moeglich. Version, Quelle und Review-Scope bleiben sichtbar.

*Preserve historical evidence. Create a linked current assessment for a new or
materially changed cloud scope; missing fields are gaps, not retroactive passes.
Justified N/A remains available, including education/development-only scopes.*

Quelle, Varianten und bekannte Quell-Unstimmigkeiten:
[C3A/C5 evidence contract](docs/c3a-c5-evidence-contract.md).
Lokale strukturelle Regression: `python3 tests/test-cloud-contract.py`.
Die Tests pruefen Vorlagen/Grenzen, nicht die Wahrheit eines Provider-Testats.

*See the linked contract for provenance and source anomalies. Structural
tests check shipped templates and boundaries, not provider-report validity.*

## Version 0.5.2 / Version 0.5.2

`v0.5.2` veröffentlicht den agentenneutralen `model-routing.json`-Vertrag für
die Komposition mit Model Routing Governance; Architekturregeln bleiben
unverändert.

*`v0.5.2` publishes the agent-neutral `model-routing.json` contract for
composition with Model Routing Governance; architecture rules are unchanged.*

## Version 0.5.1 / Version 0.5.1

`v0.5.1` ergänzt fortsetzbare Remote-Transaktionen, exakte stabile
Identifikatoren, manifestdeklarierte idempotente Post-Merge-Aktionen und die
Revalidierung direkter sowie gestapelter Abhängigkeiten.

*`v0.5.1` adds resumable remote transactions, exact stable identifiers,
manifest-declared idempotent post-merge actions, and revalidation of direct and
stacked dependencies.*

## Version 0.5.0 / Version 0.5.0

`v0.5.0` ergänzt auditfähige Spec-Kit-Run-Evidence-Felder, damit generierte
Markdown-Dokumente und Checklisten Anwendbarkeit, `N/A`-Begründung, Reviewer,
Evidence-Pfad, Restrisiko und Follow-up pro standardsrelevantem Spec-Kit-Lauf
aufzeichnen können.

*`v0.5.0` adds audit-ready Spec-Kit run evidence fields so generated Markdown
documents and checklists can record applicability, `N/A` rationale, reviewer,
evidence path, residual risk, and follow-up per standards-relevant Spec-Kit
run.*

## Kompatibilitäts- und Sicherheitsübersicht / Compatibility and Safety Summary

- kompatibel mit Spec-Kit `>=0.8.0`
- priorisiert als Stufe `20`
- ergänzt, aber ersetzt nicht `security-governance`
- trennt sichere Architektur von allgemeiner iSAQB/arc42-Architektur
- keine automatischen Cloud-, Remote-, Merge- oder Provider-Aktionen

## License

MIT. See `LICENSE`.

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

DE: v0.6.1 praezisiert bestehende Architekturvorlagen ohne neue Template-IDs,
Commands oder Schemas. Rechtliche Rollen bleiben beim projektgefuehrten
Security-Nachweis. EN: v0.6.1 clarifies existing architecture records without
new template IDs, commands or schemas; Security owns applicability.

[Quellenbindung, Grenzen und Pruefung / Sources, boundaries and checks](docs/regulatory-architecture-contract.md).
