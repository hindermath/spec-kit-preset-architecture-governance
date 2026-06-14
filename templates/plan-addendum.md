## Architecture Planning Checks

- Confirm whether runtime, hardware, or platform constraints affect MSL
  feasibility, and record the architectural reason if non-MSL is chosen.
- Confirm architecture evidence owners.
- Plan trust-boundary analysis: which boundaries are crossed, which data
  flows are involved, which data classifications apply.
- Plan threat-model updates for new or changed boundaries and data flows
  using `STRIDE`+`CIA`; add `CAPEC` references for the highest-risk paths.
- Plan how Defense in Depth, Least Privilege, Fail-Safe Defaults, and
  Attack Surface Reduction will be realised in this change.
- Plan how authentication, authorisation, logging, and input validation
  will stay implemented as cross-cutting concerns rather than ad hoc.
- Plan secret-store usage (no secrets in code or Git-tracked config).
- Plan Security Architecture Decision Records (S-ADR) for any
  architecturally significant decision in this change.
- Plan `arc42` Section 8 security cross-cutting updates (auth, encryption
  in transit and at rest, input validation, error handling, logging,
  dependencies, deployment).
- Plan security quality attribute scenarios (iSAQB CPSA-F) where
  applicable.
- Plan `Zero Trust` (NIST SP 800-207) applicability evaluation for
  distributed, service-based, cloud-near, or remote-access changes.
- Plan `OWASP SAMM` follow-up actions for long-lived projects.
- Plan `BSI C3A` cloud autonomy applicability evaluation for cloud-service
  selection, cloud operation, managed services, container/artifact hosting,
  or provider-dependent deployments. If C3A is `N/A`, plan the short
  rationale.
- Plan `BSI C5` cloud compliance assurance evaluation for cloud-service
  selection, cloud operation, managed services, container/artifact hosting,
  provider-dependent deployments, or cloud assurance reviews. If C5 is
  `N/A`, plan the short rationale.

## Audit Evidence Planning

- Plan audit-ready Markdown evidence for this Spec-Kit run, including owner, reviewer, evidence path, and standard-specific applicability.
- Plan how each relevant checkpoint will be recorded as `Applicable`, `N/A`, or `Open`.
- Plan concrete evidence updates under the default evidence directory for this preset; do not leave checklist templates unfilled.
- Treat `Open` as temporary: assign an owner, follow-up, and re-evaluation trigger.
