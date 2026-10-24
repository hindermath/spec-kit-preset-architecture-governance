# v0.6.4: Dokumentation / Documentation

## Veröffentlichungsabschluss / Publication closeout

| Feld / Field | Wert / Value | Bedeutung / Meaning |
|---|---|---|
| `candidate_status` | `HistoricalCandidate` | Ursprünglicher Vorbereitungsstand / original preparation state |
| `release_status` | `Published` | Reguläres Release, geprüft zum angegebenen Zeitpunkt / regular release checked as of the timestamp |

Tag: [v0.6.4](https://github.com/hindermath/spec-kit-preset-architecture-governance/tree/v0.6.4). Release-Commit / release commit:
`bf2261d0d7c31e1c892dfa2b9708e5978dd28a73`. [GitHub Release](https://github.com/hindermath/spec-kit-preset-architecture-governance/releases/tag/v0.6.4), veröffentlicht / published:
`2026-10-23T21:29:31.0000000+00:00`. Nachgeprüft / rechecked: `2026-10-24T10:55:24.5966620+00:00`.

[Unverändertes Tag-Archiv / unchanged tag archive](https://github.com/hindermath/spec-kit-preset-architecture-governance/archive/refs/tags/v0.6.4.zip)
mit SHA-256 / with SHA-256: `020349ca49db89c655762b1cc1ce86d5f40ea0e4b2f598aac443ed6e0dbdc6e4`.
[Maschinenlesbarer Status und Quellen / machine-readable status and sources](release-0.6.4-publication.json).

Das Paket ist veröffentlicht. Der folgende historische Vorbereitungstext
behält seinen damaligen Prüfbereich; seine Statuswörter gelten nicht als
aktueller Veröffentlichungsstand. Dieser spätere Dokumentationsnachlauf auf
main ändert weder Tag noch ZIP. Er ersetzt keine technische, fachliche oder
menschliche Freigabe und behauptet keine Consumer-Installation oder Katalogaufnahme.

<div lang="en">

The package is published. The historical preparation text below retains its
original assessment scope; its status words do not describe current publication.
This later documentation follow-up on main changes neither tag nor ZIP.
It replaces no technical, professional or human approval and claims no consumer
installation or catalogue acceptance.

</div>

Bezug / Tracking: [#342: Veröffentlichungsstatus](https://github.com/hindermath/home-baseline/issues/342)
und / and [#343: Verbesserungsprofile](https://github.com/hindermath/home-baseline/issues/343).

## Historischer Validierungsstand / Historical validation state

Unveränderter ursprünglicher Text / unchanged original text:

<!-- historical-candidate:start -->

Quellkandidat zur gesammelten Sichtung, nicht durch diesen Text veröffentlicht.
*Source candidate for collected review; this text does not publish a release.*

[Dokumentationsumfang und Prüfgrenzen / Scope and test limits](documentation-closeout.md)

Bestehende Tags und historische Nachweise bleiben unverändert. Technische und fachliche Freigaben sind getrennt.
*Existing tags and historical evidence stay unchanged. Technical and human acceptance are separate.*
<!-- historical-candidate:end -->

## Verbesserungsprofil / Improvement profile

Vergleich / comparison: [v0.5.2 → v0.6.4](https://github.com/hindermath/spec-kit-preset-architecture-governance/compare/45b7cd667e25d3ec22a14fc9f17a085b507b7bfe...bf2261d0d7c31e1c892dfa2b9708e5978dd28a73).

Ausgang / from: 45b7cd667e25d3ec22a14fc9f17a085b507b7bfe. Ziel / to: bf2261d0d7c31e1c892dfa2b9708e5978dd28a73.

### v0.6.0: Fachlicher Vertrag / Professional contract

DE: **Vorher:** Cloud-Autonomie und Provider-Nachweise waren nicht gleich präzise strukturiert. **Änderung:** C3A-Kriterien und C5-Evidence wurden explizit; Zeitpunkt, Prüfzeitraum und Wirksamkeit werden getrennt. **Nutzen:** Architekturentscheidungen lassen sich an konkrete Kriterien und echte Provider-Evidence binden.

<div lang="en">

EN: **Before:** Cloud autonomy and provider evidence lacked equally precise structure. **Change:** C3A criteria and C5 evidence became explicit; as-of-date, review period and effectiveness remain distinct. **Benefit:** Architecture decisions can be linked to concrete criteria and actual provider evidence.

</div>

Quellen / sources: [templates/c3a-criteria-catalog.json](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/45b310e53d5e361f15d48701cc2eda0a1295b554/templates/c3a-criteria-catalog.json), [templates/cloud-compliance-assurance-template.md](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/45b310e53d5e361f15d48701cc2eda0a1295b554/templates/cloud-compliance-assurance-template.md), [tests/test-cloud-contract.py](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/45b310e53d5e361f15d48701cc2eda0a1295b554/tests/test-cloud-contract.py).

### v0.6.1: Fachlicher Vertrag / Professional contract

DE: **Vorher:** Datenschutz- und Resilienzfragen benötigten klarere Entscheidungsgrenzen. **Änderung:** Vorlagen und Architekturhinweise ergänzen Datenschutz, Resilienz und begrenzte Nachweisaussagen; 0.6.2 korrigierte den Installationsbefehl. **Nutzen:** Offene Architekturfragen werden benannt, statt eine bestandene Provider- oder Produktprüfung zu behaupten.

<div lang="en">

EN: **Before:** Privacy and resilience needed clearer decision boundaries. **Change:** Templates and guidance add privacy, resilience and bounded evidence claims; 0.6.2 corrected the install command. **Benefit:** Open architecture questions remain visible instead of implying provider or product acceptance.

</div>

Quellen / sources: [templates/threat-model-template.md](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/21c0f43d1c93455c43e989de965d45c2851e824f/templates/threat-model-template.md), [templates/adr-template.md](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/21c0f43d1c93455c43e989de965d45c2851e824f/templates/adr-template.md), [tests/test-cloud-contract.py](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/21c0f43d1c93455c43e989de965d45c2851e824f/tests/test-cloud-contract.py).

### v0.6.4: Bedienbarkeit und Dokumentation / Usability and documentation

DE: **Vorher:** Ein kurzer README-Einstieg erklärte die vollständigen Leserpfade und Grenzen noch nicht gleichwertig. **Änderung:** Deutsch-/Englisch-Leitfäden, Command-/Vorlagen-Erklärungen und Dokumentationsregressionen wurden ergänzt. Frühere Einstiegsverbesserungen und der letzte Patch werden getrennt ausgewiesen. **Nutzen:** Lernende finden Voraussetzungen, Beispiel, Ergebnis und Fehlerhilfe. Neue Textklarheit ist keine neue Runtime-Funktion oder menschliche Abnahme.

<div lang="en">

EN: **Before:** The short README entry did not yet explain the complete reader journey and limits equally. **Change:** German/English guides, command/template explanations and documentation regressions were added. Earlier entry-point improvements and the final patch are reported separately. **Benefit:** Learners can find prerequisites, an example, its result and troubleshooting. Clearer text is not a new runtime feature or human acceptance.

</div>

Quellen / sources: [docs/user-guide.md](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/bf2261d0d7c31e1c892dfa2b9708e5978dd28a73/docs/user-guide.md), [docs/user-guide.EN.md](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/bf2261d0d7c31e1c892dfa2b9708e5978dd28a73/docs/user-guide.EN.md), [tests/test-documentation-closeout.ps1](https://github.com/hindermath/spec-kit-preset-architecture-governance/blob/bf2261d0d7c31e1c892dfa2b9708e5978dd28a73/tests/test-documentation-closeout.ps1).

### Zwischenstände / Intermediate versions

| Tag | Commit | Änderungsspanne / Change range |
|---|---|---|
| [v0.6.0](https://github.com/hindermath/spec-kit-preset-architecture-governance/tree/v0.6.0) | 45b310e53d5e361f15d48701cc2eda0a1295b554 | [v0.5.2 → v0.6.0](https://github.com/hindermath/spec-kit-preset-architecture-governance/compare/v0.5.2...v0.6.0) |
| [v0.6.1](https://github.com/hindermath/spec-kit-preset-architecture-governance/tree/v0.6.1) | 21c0f43d1c93455c43e989de965d45c2851e824f | [v0.6.0 → v0.6.1](https://github.com/hindermath/spec-kit-preset-architecture-governance/compare/v0.6.0...v0.6.1) |
| [v0.6.2](https://github.com/hindermath/spec-kit-preset-architecture-governance/tree/v0.6.2) | 017e91a24a685e23f176e98c07c9ac8d81487cbb | [v0.6.1 → v0.6.2](https://github.com/hindermath/spec-kit-preset-architecture-governance/compare/v0.6.1...v0.6.2) |
| [v0.6.3](https://github.com/hindermath/spec-kit-preset-architecture-governance/tree/v0.6.3) | 55106cb5e68294055f95d4fdc29a27720f04a74f | [v0.6.2 → v0.6.3](https://github.com/hindermath/spec-kit-preset-architecture-governance/compare/v0.6.2...v0.6.3) |
| [v0.6.4](https://github.com/hindermath/spec-kit-preset-architecture-governance/tree/v0.6.4) | bf2261d0d7c31e1c892dfa2b9708e5978dd28a73 | [v0.6.3 → v0.6.4](https://github.com/hindermath/spec-kit-preset-architecture-governance/compare/v0.6.3...v0.6.4) |

Zugehörige PRs / related PRs: [#6](https://github.com/hindermath/spec-kit-preset-architecture-governance/pull/6), [#7](https://github.com/hindermath/spec-kit-preset-architecture-governance/pull/7), [#9](https://github.com/hindermath/spec-kit-preset-architecture-governance/pull/9), [#8](https://github.com/hindermath/spec-kit-preset-architecture-governance/pull/8), [#11](https://github.com/hindermath/spec-kit-preset-architecture-governance/pull/11), [#10](https://github.com/hindermath/spec-kit-preset-architecture-governance/pull/10), [#12](https://github.com/hindermath/spec-kit-preset-architecture-governance/pull/12).

### Nachweise und Grenzen / Evidence and limits

Der Quellcode der verlinkten Tests belegt ihre Implementierung, nicht ihre Ausführung. Für den früheren exakten PR-Head 38f5fd4191d9f4e71bc719ccf521125c63fe7401 sind 0 erfolgreiche Check-Runs erneut lesend nachgewiesen. Details und native Runner-Namen stehen im JSON-Nachweis; [damaliger PR](https://github.com/hindermath/spec-kit-preset-architecture-governance/pull/12). Das ist historische Evidence, kein Pass des neuen Dokumentations-Heads.

<div lang="en">

Linked test code proves implementation, not execution. 0 successful check runs were rechecked for the earlier exact PR head; see the JSON for native runner names and links. These are historical results, not passes for the new documentation head.

</div>

Historische Feldtests behalten ihre eigene Version. Ein besserer Leserpfad ist keine neue Runtime-Funktion. Die Fachverträge, Rollen, Prioritäten und menschlichen Entscheidungsrechte bleiben in diesem Nachlauf unverändert. Keine neue Routing-Entwicklung, Modellprobe, Produkt-, Risiko-, Konformitäts-, WCAG- oder Zertifizierungsfreigabe.

<div lang="en">

Historical field tests retain their own version. A clearer reader path is not a new runtime feature. This follow-up changes no professional contracts, roles, priorities or human decision rights. It grants no new routing development, model probe, product, risk, compliance, WCAG or certification acceptance.

</div>

### Dokumentationsauswirkung / Documentation impact

UpdateRequired. Owner: Thorsten Hindermann. Quelle / source: unveränderliche Tags, echte Release-/Archivnachweise und verlinkte Testläufe / immutable tags, actual release/archive evidence and linked check runs. Leserpfad / reader path: README → DE/EN-Leitfaden → dieser Nachweis → Quellen und nächste sichere Aktion / this record → sources and next safe action. Zielgruppe / audience: alle vier IHK-IT-Berufe, alle vier Fachinformatik-Fachrichtungen und Entwickelnde ohne Spezialwissen / all four IT occupations and IT specialist disciplines, plus non-specialist developers. Deutsch zuerst, gleichwertiges Englisch, CEFR B2 und anwendbare WCAG 2.2 AA sind Prüfziele, keine automatische Abnahme / German first, equivalent English, B2 and applicable WCAG 2.2 AA are review targets, not automatic acceptance. Distribution: source-only; kein Home-Sync / no Home sync. Re-Evaluation: Tag-, Release-, Evidence-, Quellen- oder Scope-Drift / tag, release, evidence, source or scope drift.

Neue lokale Prüfungen und native CI werden im neuen PR am tatsächlichen Head nachgewiesen. Nächste Aktion: gesammelte menschliche Sichtung; vorher kein Merge. / New local checks and native CI are recorded in the new PR at its actual head. Next action: collected human review; no merge beforehand.
