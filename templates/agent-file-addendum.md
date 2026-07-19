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
