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
- Surface required architecture evidence under `docs/security/` (S-ADRs
  in `docs/security/adr/`).
- Document every `N/A` decision with rationale; never silently omit.
