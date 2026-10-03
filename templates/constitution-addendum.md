## Secure Architecture Governance

### Architectural security principles

AI-generated and human-written architecture MUST follow these principles
together — secure code without secure architecture is not sufficient.

- **Trust boundaries**: define explicit boundaries; validate and sanitise
  every input crossing one.
- **Defense in depth**: at least two independent security layers protect
  every critical asset.
- **Least privilege**: every component, service, and process operates with
  the minimum permissions it needs.
- **Fail-safe defaults**: deny by default, grant explicitly; error paths
  fall back into a safe state.
- **Attack surface reduction**: disable or remove unused endpoints,
  services, and debug features before release.
- **Separation of concerns**: implement authentication, authorisation,
  logging, and input validation as cross-cutting concerns rather than
  scattering them ad hoc.
- **Secure configuration**: store secrets in platform-appropriate secret
  stores (Azure Key Vault, AWS Secrets Manager, macOS Keychain, Windows
  Credential Manager). Never in source code or in Git-tracked config.
- **Supply-chain security**: dependencies from verified registries; commit
  lock files; replace known-vulnerable dependencies before release.

### Threat modeling and risk

- Threat modeling MUST use `STRIDE` (Spoofing, Tampering, Repudiation,
  Information disclosure, Denial of service, Elevation of privilege) as
  the base framework.
- Threats MUST be mapped against the `CIA` triad (Confidentiality,
  Integrity, Availability) impact.
- For the highest-risk attack paths, reference relevant `CAPEC` patterns.
- Each identified threat MUST have an explicit mitigation, an accepted-risk
  rationale, or a deferral with a re-evaluation trigger.

### Architecture documentation

- Architecturally significant decisions MUST be captured as
  `Security Architecture Decision Records` (S-ADRs) — see `adr-template`.
- Each project SHOULD maintain an `arc42` Section 8 security
  cross-cutting concepts document — see `arc42-security-template`,
  covering authentication, authorisation, encryption in transit and at
  rest, input validation, error handling, logging, dependencies, and
  deployment security.
- Long-lived projects SHOULD record security quality attribute scenarios
  using the `iSAQB CPSA-F` quality scenario method — see
  `security-quality-scenarios-template`.

### Zero Trust and SAMM

- `Zero Trust` (NIST SP 800-207) applicability MUST be evaluated explicitly
  for distributed, service-based, cloud-near, or remotely managed systems.
- Long-lived projects and workspaces SHOULD use `OWASP SAMM` to inform
  improvement plans across Governance, Design, Implementation,
  Verification, and Operations.

### Cloud autonomy and digital sovereignty

- `BSI C3A` (Criteria enabling Cloud Computing Autonomy) applicability MUST
  be evaluated explicitly when a project selects, operates, or materially
  depends on cloud services, including SaaS, PaaS, IaaS, managed services,
  container registries, artifact hosting, or provider-dependent deployments.
- C3A is a guiding transparency framework for self-determined cloud use,
  not a direct legal obligation by itself. Record the decision as
  `Applicable`, `N/A`, or `Open` using
  `cloud-autonomy-applicability-template`.
- When applicable, architecture evidence MUST identify cloud-service
  selection rationale, provider dependencies, available audit or assurance
  evidence, autonomy and lock-in risks, exit or portability concerns, and
  links to related S-ADRs, Zero Trust notes, or C5/C3A evidence.
- Cloud use limited to generic development infrastructure (for example
  GitHub/GitLab hosting without released or operated cloud runtime) MAY be
  documented as `N/A` with a short toolchain rationale.

### Cloud compliance assurance

- `BSI C5` (Cloud Computing Compliance Criteria Catalogue) applicability
  SHOULD be evaluated explicitly when a project selects, operates, or
  materially depends on cloud services, including SaaS, PaaS, IaaS, managed
  services, container registries, artifact hosting, or provider-dependent
  deployments.
- C5 is an assurance and auditability framework for cloud use, not a blanket
  requirement for private learning projects. Record the decision as
  `Applicable`, `N/A`, or `Open` using
  `cloud-compliance-assurance-template`.
- When applicable, architecture evidence SHOULD identify C5 testat/report
  status, assurance scope, shared-responsibility gaps, provider and
  subprocessor dependencies, data location, logging, backup, incident
  evidence, and links to related C3A records, Zero Trust notes, or S-ADRs.
- Cloud use limited to generic development infrastructure MAY be documented
  as `N/A` with a short toolchain rationale.

### Memory-safe language interaction

- Treat `MSL` feasibility as an architectural runtime constraint when
  platform or runtime choices are involved. Record the architectural
  reason for any non-MSL choice — do not duplicate code-level secure-code
  generation rules here; those live in the `security-governance` preset.

### Evidence locations

- Architecture evidence defaults to `docs/security/`.
- S-ADRs default to `docs/security/adr/` as one file per decision.
- Threat models, arc42 security concepts, Zero Trust notes, SAMM
  assessments, cloud autonomy applicability records, cloud compliance
  assurance records, and security quality scenarios live alongside in
  `docs/security/`.

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
