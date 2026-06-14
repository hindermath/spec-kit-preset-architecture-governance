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
