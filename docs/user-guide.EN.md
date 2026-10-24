# User guide: architecture-governance

<!-- current-package: 0.6.5 -->

Package identity: **v0.6.5**. [Preparation and publication boundary](release-0.6.5-validation.md). The release page, not this preparation snapshot, proves publication and the external archive hash. Earlier version records below remain historical.

[Release-Abschluss und Verbesserungsprofil / Publication closeout and improvement profile](release-0.6.4-validation.md).

The linked base-package evidence remains historical; this package includes the source corrections as a new version.

[Deutsch](user-guide.md) · [Preset reference](../README.md)

Historical base package **v0.6.4**. Verify the actually published version on the [release page](https://github.com/hindermath/spec-kit-preset-architecture-governance/releases). This guide grants no merge, release or project authority.

Contents: [Start](#start) · [Example](#example) · [Terms](#terms) · [Routing](#routing) · [Troubleshooting](#help) · [References](#references)

<a id="start"></a>

## Start and audience

Make system-structure security decisions traceable, separately from code-level security verification.

For apprentices in all four IHK IT occupations: IT specialists (application development, systems integration, data/process analysis, digital networking), IT systems electronics technicians, digitalisation management specialists and IT systems management specialists. Also for developers without specialist governance knowledge. You do not need to edit hashes or invent model IDs to ask for the next step. Ask the maintainer to check technical bindings.

Use an already initialized Spec Kit target repository. Read the prerequisites and installation instructions in the preset reference first; replace example paths. A template is a starter, not completed evidence. Installation adds instructions and files; it does not start a feature or grant approval.

Input: Describe the external integration, affected data and trust boundaries.

<a id="example"></a>

## One complete example

1. Describe the bounded task and existing files. Do not silently widen scope.
2. Use the following example in the agent chat. It is a prompt, not a shell command:

~~~text
Use threat-model-template and adr-template. Plan docs/security/threat-model.md and a security ADR with alternatives and verification tasks. Do not claim a completed review.
~~~

3. Data flow, boundaries, threats and reasoned decisions are discoverable. Cloud and regulatory questions reference existing project-owned evidence.
4. Check the result and recorded next action. Changes, repair, feature execution and delivery each need their applicable authority. A passing technical check is not human acceptance.

Read-only installation check in the initialized target repository:

~~~text
specify preset info architecture-governance
specify preset resolve threat-model-template
~~~

Resolve reports the selected template source; it does not fill in or execute that template.

<a id="terms"></a>

## Terms and evidence

- **S-ADR:** Security Architecture Decision Record: security decision with alternatives and consequences.
- **Zero Trust:** Do not trust access merely because of network location; verify identity, permissions and context.
- **Cloud-Assurance:** Traceable review of provider and customer responsibilities, not automatic certification.

Where the existing contract uses these values: Applicable means relevant, not passed; N/A needs a reason; Open needs the recorded next action and responsible person. This explanation adds no fields to existing schemas. Keep genuine historical evidence; never edit a hash or approval just to make a check pass.

<a id="routing"></a>

## Stable routing and explicit actions

| Command | Declared role |
|---|---|
| `speckit.specify` | `frontier-reasoning` |
| `speckit.plan` | `frontier-reasoning` |
| `speckit.tasks` | `frontier-reasoning` |

Roles describe tasks, not a model name or quality guarantee. Read the actual model-routing.json contract; generic examples such as coding-review do not override a stronger command requirement. The existing autonomous runner retains the strongest overlapping role, independently of installation priority. Merely installing a role contract does not switch a live chat or configure personal profiles.

A model-free script check and an agent assessment are different activities. Model calls, including model-access preflights, can consume quota even when they are read-only. No probe or provider switch is authorized by this documentation. No new dynamic-routing implementation is included.

Package version, schema version and historical field test are different facts. Earlier acceptance applies only to its recorded scope and source state.

<a id="help"></a>

## Troubleshooting and safe next action

Do not mark cloud checks passed when scope is unclear. General architecture belongs to the iSAQB preset; it does not replace security review.

If a command or template is missing, inspect preset info and the manifest below. Check the documented minimum tools and enabled installation. Resolve ambiguity with the maintainer; do not change policy, disable validators or claim an unperformed test. A safety blocker remains a blocker.

This language/accessibility pass targets CEFR B2 and applicable WCAG 2.2 AA. Static tests do not certify that target. Screen-reader, Braille and representative-user tests not actually performed remain unverified.

<a id="references"></a>

## Templates and deeper reference

- [`threat-model-template`](../templates/threat-model-template.md)
- [`adr-template`](../templates/adr-template.md)
- [`arc42-security-template`](../templates/arc42-security-template.md)
- [`security-quality-scenarios-template`](../templates/security-quality-scenarios-template.md)
- [`zero-trust-applicability-template`](../templates/zero-trust-applicability-template.md)
- [`samm-assessment-template`](../templates/samm-assessment-template.md)
- [`cloud-autonomy-applicability-template`](../templates/cloud-autonomy-applicability-template.md)
- [`c3a-criteria-catalog`](../templates/c3a-criteria-catalog.json)
- [`cloud-compliance-assurance-template`](../templates/cloud-compliance-assurance-template.md)

These names identify available starters; they are not an instruction to create every file. Reuse existing suitable evidence. JSON field names remain technical identifiers, not translated keys.

- [Manifest and prerequisites](../preset.yml)
- [Stable command-role contract](../model-routing.json)
- [Documentation scope, review and test limits](documentation-closeout.md)
