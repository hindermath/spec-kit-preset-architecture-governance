# C3A/C5: Quellen- und Evidence-Vertrag / Source and evidence contract

## Quelle / Source

Owner: Thorsten Hindermann. Documentation Impact: `UpdateRequired`.
Readers: maintainers, architects and coding agents through README, addenda
and wrapped Specify/Plan/Tasks commands. Canonical source: this preset's
templates and versioned JSON catalogue. Distribution: preset source/package;
no host installation, Home sync or product approval is granted by this document.
Reevaluate on catalogue change or materially changed cloud scope.

- [BSI C3A v1.0, 2026-04-27](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/CloudComputing/C3A_Cloud_Computing_Autonomy.pdf?__blob=publicationFile&v=5)
- PDF SHA-256: `d985b4e7a9969aefda5882a02eeaf4fd97636b2a3ae30f868b25c01a5dcffe2d`
- [BSI C5:2026](https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/CloudComputing/ComplianceControlsCatalogue/2026/C5_2026.pdf?__blob=publicationFile&v=6),
  section 3.4.4, page 27: Type 1 as-of-date; Type 2 operating effectiveness over
  a period. Record the actual report's criteria version, not an assumed default.

## Kriterienmodell / Criteria model

DE: Das JSON bindet 30 Gruppen in sechs Domaenen (4/3/5/10/5/3): strategische,
rechtliche, Daten-, operative, Lieferketten- und Technologiesouveraenitaet.
Gruppennamen, Startseite und C-/AC-/SI-Kennungen sind mit dem Original
abgeglichen. Die verbindlichen Anforderungstexte bleiben im BSI-Katalog;
diese Zuordnung ersetzt sie nicht. Die Detailvorlage bindet ausgewaehlte
Varianten an Katalogversion und Seite. Varianten sind keine allgemeine
Reifegradleiter: bei Datenorten koennen mehrere Anforderungen relevant sein.
AC muss bewusst gewaehlt oder begruendet ausgeschlossen werden. SI dient
der Auslegung und ist kein eigenstaendiger bestandener Kontrollpunkt.

EN: The JSON binds all 30 groups in six domains (4/3/5/10/5/3): strategic,
legal, data, operational, supply-chain and technology sovereignty. Group
names, starting pages and C/AC/SI identifiers were checked against the
original. Consult the bound BSI source for normative wording and exact
variant semantics; this index does not replace it. Variants are not a generic
maturity scale and several can apply within a scope. Select or justify
excluding additional criteria. SI provides interpretation, not a passed control.

Known source anomalies are retained transparently:

- SOV-4-01-C3 is headed “Additional criterion” in the source; its suffix
  remains C3 rather than being invented as AC.
- The SOC text refers to SOV-4-10 for disconnection, while the actual
  Disconnect group is SOV-4-09.
- Reconnect refers to SOV-4-9-C; the catalogue's group identifier is
  SOV-4-09. These cross-reference inconsistencies do not rename groups.

## Evidence-Grenzen / Evidence boundaries

DE: C3A setzt eine C5-Sicherheitsgrundlage voraus; fehlende Grundlage bleibt
offen. SOV-7 (Sicherheit) und SOV-8 (Umwelt) sind nicht Teil dieser 30 Gruppen.
C5 und C3A bleiben getrennte Bewertungen. Typ 1 prueft den Zeitpunkt, Typ 2
die Wirksamkeit im dokumentierten Zeitraum. Ein unbekannter Typ wird nicht
hochgestuft. Ein Report braucht Datum, Version, Scope, Ausnahmen,
Kundenverantwortung und Quellenbezug. Ein Link alleine ist keine Abnahme.

EN: C3A assumes a C5 security foundation; unavailable foundation evidence
remains an open gap. SOV-7/security and SOV-8/environment are outside these
30 groups. Keep C5 and C3A assessments separate. Type 1 is point-in-time;
Type 2 covers operating effectiveness over the recorded period. Never
upgrade Unknown by assumption. Record report date, criteria version, scope,
exceptions, customer responsibilities and evidence origin. A link is not acceptance.

Preserve previous thematic sections as summaries linked to criterion detail.
Historical records remain unchanged. Current scope reviews need current
evidence or explicit gaps, without retroactively treating missing fields as
passed. No new mandatory provider audit is introduced for educational projects.

## Komposition / Composition

Security Governance v0.6.2's standard-applicability and security/compliance
templates were reviewed. They delegate architectural C3A/C5 evidence here
and disclaim provider certification; no contradictory Type 1/Type 2 claim
or sibling edit is needed. Priority 10 security and priority 20 architecture
remain separate; command IDs, routing and minimum Spec Kit version are unchanged.
The coordinated Intake patches change series validation, not cloud assurance.

Structural tests cover identifiers, variants, AC/SI, default-open rows,
manifest wiring, command placeholders and guardrail propagation. Native
macOS/Linux/Windows CI checks portability and unchanged tracked files.
These tests are not a C5/C3A audit, provider validation, legal opinion or
product acceptance. PDF accessibility and provider-controlled external
evidence are not claimed as tested.
