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

### Memory-safe language interaction

- Treat `MSL` feasibility as an architectural runtime constraint when
  platform or runtime choices are involved. Record the architectural
  reason for any non-MSL choice — do not duplicate code-level secure-code
  generation rules here; those live in the `security-governance` preset.

### Evidence locations

- Architecture evidence defaults to `docs/security/`.
- S-ADRs default to `docs/security/adr/` as one file per decision.
- Threat models, arc42 security concepts, Zero Trust notes, SAMM
  assessments, cloud autonomy applicability records, and security quality
  scenarios live alongside in `docs/security/`.
