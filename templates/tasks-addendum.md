## Architecture Tasks

- Add explicit `STRIDE`+`CIA` threat-modeling tasks when boundaries or
  data flows change. Add `CAPEC` reference tasks for the highest-risk
  paths.
- Add Security Architecture Decision Record (S-ADR) tasks when
  architecturally significant decisions are introduced or revised, using
  `adr-template`.
- Add `arc42` Section 8 security update tasks for changes to
  authentication, authorisation, encryption in transit/at rest, input
  validation, error handling, logging, dependencies, or deployment.
- Add security quality attribute scenario tasks (iSAQB CPSA-F) where the
  feature introduces or changes security-relevant qualities.
- Add `Zero Trust` (NIST SP 800-207) applicability tasks for distributed,
  service-based, cloud-near, or remote-access systems.
- Add `OWASP SAMM` follow-up tasks for long-lived projects whose maturity
  posture is touched by this change.
- Add `BSI C3A` cloud autonomy applicability tasks for cloud-service
  selection, cloud operation, managed services, container/artifact hosting,
  or provider-dependent deployments. Use
  `cloud-autonomy-applicability-template`.
- Add evidence-update tasks under `docs/security/` for each new or
  changed artefact (S-ADR, threat model, arc42 security concept, Zero
  Trust note, SAMM assessment, cloud autonomy applicability, quality
  scenarios).
- Add a task to verify Defense in Depth, Least Privilege, Fail-Safe
  Defaults, Attack Surface Reduction, and Separation of Concerns are
  realised in the implementation, not just documented.
