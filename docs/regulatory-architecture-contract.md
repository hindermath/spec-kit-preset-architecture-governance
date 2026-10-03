# Regulatorischer Architekturvertrag / Regulatory architecture contract

Stand / Date: 2026-10-03. Owner: Thorsten Hindermann.
Documentation Impact: UpdateRequired. Release candidate: v0.6.1.

DE: Fachliche Quelle der Anwendbarkeit sind die projektgefuehrten Security-
Nachweise, insbesondere die Vorlagen von Security Governance v0.7.0.
Architecture bewertet die zugehoerigen Datenfluesse und technischen Entscheidungen.
Ohne installiertes Security-Preset sind gleichwertige projektgefuehrte
Nachweise zulaessig; es entsteht keine neue harte Paketabhaengigkeit.
EN: Project Security records, including Security v0.7.0 starters where used,
own applicability. Architecture records corresponding data flows and design
choices. Equivalent project-owned evidence is valid without an installed
Security preset; no new hard package dependency is introduced.

## Nachweis und Kompatibilitaet / Evidence and compatibility

DE: Bestehende IDs, Commands, Routing, Mindestversion und 18 bereitgestellte
Eintraege bleiben erhalten. C3A-/C5-Katalog, Typ-1-/Typ-2-Grenzen und Cloud-
Regression bleiben unveraendert. Privacy by Design/Default, Datenminimierung,
Empfaenger/Region, Loeschung, KI-Vertrauensgrenzen sowie NIS2-/DORA-Resilienz
ergaenzen bestehende Vorlagen. Keine neuen Produkt-APIs oder Evidence-Schemas.
EN: Preserve existing IDs, commands, routing, minimum version and 18 entries.
C3A/C5 catalogue and Type 1/2 semantics remain unchanged. Extend existing
records with privacy, data flows, AI boundaries and role-bound resilience.
No new product APIs or evidence schemas.

Sources: [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj),
[AI Act](https://eur-lex.europa.eu/eli/reg/2024/1689/oj),
[CRA](https://eur-lex.europa.eu/eli/reg/2024/2847/oj),
[NIS2](https://eur-lex.europa.eu/eli/dir/2022/2555/oj),
[DORA](https://eur-lex.europa.eu/eli/reg/2022/2554/oj).
Exact legal versions, dates, roles and unresolved source access are recorded
in the Security contract and project record, not inferred here.

DE: Lokale und native Cloud-Vertragstests pruefen Struktur/Komposition,
keine Rechtskonformitaet. Fachliche Sichtung der geaenderten Architektur-
und README-Aussagen erfolgt vor Merge und stabiler Veroeffentlichung.
EN: Local/native tests check structure/composition, not legal compliance.
Semantic review precedes merge and stable publication.

Audience: maintainers, learners, architects and privacy/compliance reviewers.
Reader path: README -> this contract -> S-ADR/data flows -> project Security record.
Language partner: DE-first/EN-second inline. Distribution: sourceOnly preset;
no standalone Home sync. Reevaluation: legal, role, data, AI or service change.
