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
- Add `BSI C5` cloud compliance assurance tasks for cloud-service
  selection, cloud operation, managed services, container/artifact hosting,
  provider-dependent deployments, or cloud assurance reviews. Use
  `cloud-compliance-assurance-template`.
- Add evidence-update tasks under `docs/security/` for each new or
  changed artefact (S-ADR, threat model, arc42 security concept, Zero
  Trust note, SAMM assessment, cloud autonomy applicability, cloud
  compliance assurance, quality scenarios).
- Add a task to verify Defense in Depth, Least Privilege, Fail-Safe
  Defaults, Attack Surface Reduction, and Separation of Concerns are
  realised in the implementation, not just documented.

## Audit Evidence Tasks

- Add tasks to create or update the Markdown evidence/checklist documents for this Spec-Kit run.
- Each task must name the target evidence file, the standard or governance checkpoint, and the expected decision: `Applicable`, `N/A`, or `Open`.
- Add tasks to fill evidence rows with reviewer, date, evidence path, residual risk, and follow-up where relevant.
- Add tasks to verify that no relevant checkpoint was silently omitted.
