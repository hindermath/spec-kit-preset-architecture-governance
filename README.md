# Architecture Governance Preset

Version: `0.4.0`
Requires: `spec-kit >= 0.8.0` (uses the `wrap` and `append` composition
strategies introduced in 0.8.x).

Purpose:

- inject secure-software-architecture, threat-modeling, and cloud-autonomy
  expectations into Spec Kit workflows
- keep architecture concerns separate from the more tactical
  secure-development preset; the two compose cleanly side by side
- keep secure-architecture concerns separate from the general
  iSAQB/arc42 architecture method preset

Relationship to `isaqb-architecture-governance`:

- `isaqb-architecture-governance` covers general software architecture:
  architecture goals, context, building blocks, runtime view, deployment
  view, quality scenarios, ADRs, risks, and technical debt.
- `architecture-governance` covers secure architecture: trust
  boundaries, threat modeling, STRIDE/CAPEC, Zero Trust, S-ADRs, OWASP
  SAMM, BSI C3A cloud autonomy applicability, and BSI C5 cloud assurance.
- If both general and security-relevant architecture are in scope, use
  both presets together.

Primary source chapters from `home-baseline` constitution:

- `XI. Memory-Safe Languages (MSL) Preference for Level-2 Projects` as a
  runtime-constraint input
- `XIII. Secure Software Architecture`
- architecture-related applicability rules from `XIV`
- `XVII. Threat Modeling & Attack Pattern Coverage`
- `XVIII. Zero Trust Applicability & Security Program Maturity`

Standards and concepts in scope:

- `MSL-aware runtime choice`
- `Trust Boundaries`, `Defense in Depth`, `Least Privilege`,
  `Fail-Safe Defaults`, `Attack Surface Reduction`,
  `Separation of Concerns`, `Secure Configuration`,
  `Supply-Chain Security`
- `STRIDE`+`CIA` threat modelling with `CAPEC` references for high-risk
  paths
- `arc42` Section 8 security cross-cutting concepts
- `Security Architecture Decision Records` (S-ADRs)
- `iSAQB CPSA-F` security quality attribute scenarios
- `Zero Trust` (NIST SP 800-207)
- `OWASP SAMM`
- `BSI C3A` (Criteria enabling Cloud Computing Autonomy) as a conditional
  cloud sovereignty and autonomy applicability check
- `BSI C5` (Cloud Computing Compliance Criteria Catalogue) as a conditional
  cloud compliance and assurance check

Preset strategy:

- append architecture-governance sections to `constitution-template`,
  `spec-template`, `plan-template`, and `tasks-template`
- provide a standalone agent-guidance addendum template for projects that
  maintain agent instruction files
- wrap `speckit.specify`, `speckit.plan`, and `speckit.tasks` with a
  shared architecture workflow
- provide starter templates for threat models, S-ADRs, arc42 Section 8
  security concepts, security quality scenarios, Zero Trust applicability,
  OWASP SAMM assessment, BSI C3A cloud autonomy applicability, and BSI C5
  cloud compliance assurance

Evidence templates included:

- `threat-model-template` (STRIDE × CIA matrix, CAPEC mapping, risk
  scoring)
- `adr-template` (S-ADR with compliance evidence table)
- `arc42-security-template` (auth, authorisation, encryption in
  transit/at rest, validation, error handling, logging, dependencies,
  deployment)
- `security-quality-scenarios-template` (iSAQB CPSA-F)
- `zero-trust-applicability-template` (NIST SP 800-207 tenets)
- `samm-assessment-template`
- `cloud-autonomy-applicability-template` (BSI C3A Applicable/N/A record
  for cloud service selection, provider dependencies, audit evidence, and
  autonomy risks)
- `cloud-compliance-assurance-template` (BSI C5 Applicable/N/A record for
  cloud testat/report status, assurance scope, shared-responsibility gaps,
  provider/subprocessor dependencies, data location, logging, backup, and
  incident evidence)

Default evidence location: `docs/security/`. S-ADRs default to
`docs/security/adr/` as one file per decision.

When to use:

- projects with explicit trust boundaries, distributed services, or
  meaningful integration surfaces
- teams that want documented threat models and S-ADRs as first-class
  artefacts
- systems that need a reusable Zero Trust or SAMM discussion surface
- projects selecting, operating, or depending on cloud services where
  digital sovereignty, provider dependency, audit evidence, or exit risk
  must be made explicit
- projects that need cloud assurance evidence for C5 testat/report status,
  shared responsibility, data location, logging, backup, or incident response

When not to use:

- tiny scripts or throwaway prototypes with no meaningful architecture
  surface
- teams that only want code-level secure-development prompts (use
  `security-governance` instead or in combination)
- projects with no released or operated cloud runtime where cloud use is
  limited to general development infrastructure; record C3A/C5 as `N/A`
  instead of creating unnecessary evidence

MSL note:

- this preset references MSL only as an architectural runtime constraint
- the primary MSL governance surface remains in `security-governance`

Recommended standalone install priority:

- `20`
