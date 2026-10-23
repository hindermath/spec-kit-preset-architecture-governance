# Nutzungsleitfaden: architecture-governance

<!-- current-package: 0.6.4 -->

[English](user-guide.EN.md) · [Preset-Referenz](../README.md)

Quellkandidat **v0.6.4**. Den tatsächlich veröffentlichten Stand auf der [Release-Seite](https://github.com/hindermath/spec-kit-preset-architecture-governance/releases) prüfen. Dieser Leitfaden erteilt keine Merge-, Release- oder Projektfreigabe.

Inhalt: [Start](#start) · [Beispiel](#example) · [Begriffe](#terms) · [Routing](#routing) · [Fehlerhilfe](#help) · [Referenzen](#references)

<a id="start"></a>

## Start und Zielgruppe

Sicherheitsentscheidungen zur Systemstruktur nachvollziehbar machen, getrennt von der codebezogenen Security-Prüfung.

Für Auszubildende aller vier IHK-IT-Berufe: Fachinformatiker*innen (Anwendungsentwicklung, Systemintegration, Daten- und Prozessanalyse, Digitale Vernetzung), IT-System-Elektroniker*innen, Kaufleute für Digitalisierungsmanagement und Kaufleute für IT-System-Management. Ebenso für Entwickelnde ohne Governance-Spezialwissen. Du musst zum Einstieg keine Hashes bearbeiten oder Modell-IDs erfinden. Technische Bindungen mit der Betreuung prüfen.

Nutze ein bereits mit Spec Kit initialisiertes Ziel-Repository. Lies zuerst Voraussetzungen und Installation in der Preset-Referenz; ersetze Beispielpfade. Eine Vorlage ist ein Starter, kein ausgefüllter Nachweis. Installation ergänzt Anweisungen und Dateien; sie startet kein Feature und erteilt keine Freigabe.

Eingabe: Beschreibe die externe Integration, betroffene Daten und Vertrauensgrenzen.

<a id="example"></a>

## Ein vollständiges Beispiel

1. Beschreibe den begrenzten Auftrag und vorhandene Dateien. Scope nicht still erweitern.
2. Nutze das folgende Beispiel im Agentenchat. Es ist ein Prompt, kein Shell-Befehl:

~~~text
Nutze threat-model-template und adr-template. Plane docs/security/threat-model.md und einen Security-ADR mit Alternativen und Prüfaufgaben. Kein abgeschlossenes Review behaupten.
~~~

3. Datenfluss, Grenzen, Bedrohungen und begründete Entscheidungen sind auffindbar. Cloud- und Regulierungsfragen verweisen auf vorhandene projektgeführte Evidence.
4. Prüfe Ergebnis und dokumentierte nächste Aktion. Änderungen, Reparatur, Feature-Ausführung und Lieferung brauchen jeweils die passende Autorität. Ein grüner technischer Check ist keine menschliche Abnahme.

Lesende Installationsprüfung im initialisierten Ziel-Repository:

~~~text
specify preset info architecture-governance
specify preset resolve threat-model-template
~~~

Resolve zeigt die ausgewählte Vorlagenquelle; es füllt die Vorlage nicht aus und führt sie nicht aus.

<a id="terms"></a>

## Begriffe und Nachweise

- **S-ADR:** Security Architecture Decision Record: dokumentierte Sicherheitsentscheidung mit Alternativen und Folgen.
- **Zero Trust:** Zugriffe nicht allein wegen ihres Netzes vertrauen; Identität, Rechte und Kontext prüfen.
- **Cloud-Assurance:** Nachvollziehbare Prüfung von Anbieter- und Kundenpflichten; kein automatisches Zertifikat.

Wo der bestehende Vertrag diese Werte verwendet: Applicable bedeutet anwendbar, nicht bestanden; N/A braucht einen Grund; Open braucht die dokumentierte nächste Aktion und zuständige Person. Diese Erklärung ergänzt keine Schema-Felder. Echte historische Evidence erhalten; Hash oder Freigabe niemals nur zum Bestehen einer Prüfung ändern.

<a id="routing"></a>

## Stabiles Routing und ausdrückliche Aktionen

| Command | Deklarierte Rolle |
|---|---|
| `speckit.specify` | `frontier-reasoning` |
| `speckit.plan` | `frontier-reasoning` |
| `speckit.tasks` | `frontier-reasoning` |

Rollen beschreiben Aufgaben, keinen Modellnamen und keine Qualitätsgarantie. Maßgeblich ist model-routing.json; allgemeine Beispiele wie coding-review ersetzen keine stärkere Command-Anforderung. Der bestehende autonome Runner verwendet die stärkste überlappende Rolle, unabhängig von der Installationspriorität. Die Installation eines Rollenvertrags stellt keinen laufenden Chat um und richtet keine persönlichen Profile ein.

Eine modellfreie Skriptprüfung und eine Agentenbewertung sind verschiedene Tätigkeiten. Modellaufrufe, auch Zugangs-Preflights, können trotz read-only-Verhalten Kontingent verbrauchen. Diese Dokumentation beauftragt keine Probe und keinen Anbieterwechsel. Sie enthält keine neue dynamische Routing-Implementierung.

Paketversion, Schema-Version und historischer Feldtest sind verschiedene Angaben. Eine frühere Abnahme gilt nur für ihren belegten Scope und Quellenstand.

<a id="help"></a>

## Fehlerhilfe und sichere nächste Aktion

Bei unklarem Cloud-Scope keine Checkliste pauschal als bestanden markieren. Allgemeine Architektur liegt beim iSAQB-Preset; es ersetzt kein Security-Review.

Fehlt ein Command oder eine Vorlage, zuerst preset info und das unten verlinkte Manifest prüfen. Mindestwerkzeuge und aktive Installation prüfen. Unklarheit mit der Betreuung klären; weder Policy ändern, Validatoren abschalten noch einen nicht ausgeführten Test behaupten. Eine Schutzsperre bleibt eine Sperre.

Diese Sprach- und Zugänglichkeitsrunde zielt auf CEFR B2 und anwendbare WCAG 2.2 AA. Statische Tests bescheinigen das Ziel nicht. Nicht tatsächlich ausgeführte Screenreader-, Braille- und Nutzendentests bleiben ungeprüft.

<a id="references"></a>

## Vorlagen und Vertiefung

- [`threat-model-template`](../templates/threat-model-template.md)
- [`adr-template`](../templates/adr-template.md)
- [`arc42-security-template`](../templates/arc42-security-template.md)
- [`security-quality-scenarios-template`](../templates/security-quality-scenarios-template.md)
- [`zero-trust-applicability-template`](../templates/zero-trust-applicability-template.md)
- [`samm-assessment-template`](../templates/samm-assessment-template.md)
- [`cloud-autonomy-applicability-template`](../templates/cloud-autonomy-applicability-template.md)
- [`c3a-criteria-catalog`](../templates/c3a-criteria-catalog.json)
- [`cloud-compliance-assurance-template`](../templates/cloud-compliance-assurance-template.md)

Diese Namen bezeichnen verfügbare Starter; sie sind kein Auftrag, jede Datei anzulegen. Vorhandene passende Evidence weiterverwenden. JSON-Feldnamen bleiben technische Bezeichner, keine zu übersetzenden Schlüssel.

- [Manifest und Voraussetzungen](../preset.yml)
- [Stabiler Command-Rollenvertrag](../model-routing.json)
- [Dokumentationsumfang, Sichtung und Prüfgrenzen](documentation-closeout.md)
