# Security Architecture Cross-Cutting Concepts (arc42 Section 8)

## Spec-Kit Run Evidence

- Feature / Spec ID:
- Spec-Kit phase: [specify / plan / tasks / implement / review / release]
- Branch / commit / PR:
- Run date:
- Evidence owner:
- Reviewer:
- Standards / criteria checked: ISO 27001/27002 secure architecture controls, STRIDE, CAPEC, arc42, iSAQB CPSA-F, NIST Zero Trust, OWASP SAMM, BSI C3A, BSI C5
- Decision: [Applicable / N/A / Open]
- Evidence path:
- N/A rationale, if not applicable:
- Open follow-up owner and trigger:
- Re-evaluation trigger:
- Certification-readiness note: Use this record as architecture and cloud-assurance evidence; C5 evidence must link actual reports/testats where available and record customer-side review responsibility.

## Audit Evidence Matrix

| Checkpoint / control reference | Applicability | Evidence produced or linked | Result | Residual risk / rationale |
| --- | --- | --- | --- | --- |
| Spec-Kit run scope is identified | [Applicable / N/A / Open] | | [OK / Open / N/A] | |
| Standard-specific criteria are mapped | [Applicable / N/A / Open] | | [OK / Open / N/A] | |
| Evidence artefact path is recorded | [Applicable / N/A / Open] | | [OK / Open / N/A] | |
| N/A decisions are justified | [Applicable / N/A / Open] | | [OK / Open / N/A] | |
| Open findings have owner and trigger | [Applicable / N/A / Open] | | [OK / Open / N/A] | |

## Context

- System or release:
- Owner:
- Date:
- Related S-ADRs:
- Related threat model entries:

## 8.1 Authentication

- User authentication mechanism (password + MFA, OIDC, SAML, mTLS, …):
- Service-to-service authentication (mTLS, signed tokens, workload
  identity):
- Credential storage (where; rotation policy):
- Session establishment and revocation:

## 8.2 Authorisation

- Access control model (RBAC, ABAC, ReBAC, capability-based):
- Policy decision point and policy enforcement point:
- Privilege boundaries (least privilege application):
- Administrative-action approval flow:

## 8.3 Encryption in Transit

- Transport protocols and minimum versions (e.g. TLS 1.2+):
- Certificate management and rotation:
- Inter-service encryption boundaries:
- Mutual TLS where required:

## 8.4 Encryption at Rest

- Storage encryption (database, object store, message queue, file
  system):
- Key management (KMS / HSM / Key Vault / Keychain):
- Key rotation cadence:
- Backup encryption:

## 8.5 Input Validation and Output Encoding

- Validation strategy at trust boundaries (allowlists, schema
  validation):
- Output encoding strategy (HTML, JS, URL, SQL, shell):
- Centralised validation library or pattern (separation of concerns):

## 8.6 Error Handling and Resilience

- Error categorisation (user-facing vs internal):
- No internal state, stack traces, or connection strings exposed
  externally:
- Fail-safe default behaviour:
- Circuit-breaker, retry, timeout policies:

## 8.7 Logging and Monitoring

- Log categories (audit, security, application, access):
- Log retention and integrity:
- Sensitive-data handling in logs (no secrets, no full PII):
- Alerting and incident escalation paths:

## 8.8 Secrets and Configuration

- Secret store (Azure Key Vault, AWS Secrets Manager, macOS Keychain,
  Windows Credential Manager, HashiCorp Vault):
- Secret-injection mechanism (env vars, sidecar, mounted file):
- Configuration tiering (default / per-environment / per-tenant):
- No secrets in source or Git-tracked config:

## 8.9 Dependencies and Supply Chain

- Verified registries used:
- Lock files committed:
- Dependency-scanning automation (Renovatebot/Dependabot, Dependency
  Track, Scorecard):
- Build provenance and SBOM artefact location:
- VEX disposition policy for known vulnerabilities:

## 8.10 Deployment Security

- Build platform isolation:
- Artefact signing and verification:
- Deployment authentication (workload identity, OIDC tokens, signed
  manifests):
- Runtime hardening (read-only file systems, dropped capabilities,
  network policies):
- Rollback and incident-response posture:

## Cross-References

- ASVS verification (with Level):
- Zero Trust applicability note:
- SAMM assessment entry:
