# honkai-star-rail-helper

`honkai-star-rail-helper` ist ein Dienstprogramm, das entwickelt wurde, um Charakterdaten, Fähigkeiten und Relikt-Empfehlungen für das Videospiel [Honkai: Star Rail](https://en.wikipedia.org/wiki/Honkai:_Star_Rail) zu verwalten und zu verarbeiten. Es liest Eingabedateien, verarbeitet verschiedene Attribute wie Charakterinformationen und Fähigkeitssets und gibt die Ergebnisse in einem organisierten Format aus. Die Eingabedaten stammen aus den offiziellen Update-Paketen im Repository [StarRailData](https://github.com/Dimbreath/StarRailData/t...

## Neueste Charaktertabelle
<!-- CHARACTER_TABLE_START -->
| DAMAGE_TYPE | RARITY | DESTRUCTION               | THE_HUNT  | ERUDITION | HARMONY   | NIHILITY                  | PRESERVATION       | ABUNDANCE  |
|-------------|--------|---------------------------|-----------|-----------|-----------|---------------------------|--------------------|------------|
| PHYSICAL    | 5      | clara\|player\|yunli      | boothill  | argenti   | robin     |                           |                    |            |
| PHYSICAL    | 4      |                           | sushang   |           | hanya     | luka                      |                    | natasha    |
| FIRE        | 5      | sam                       | topaz     | himeko    |           | jiaoqiu                   | player2            | lingsha    |
| FIRE        | 4      | hook                      |           |           | asta      | guinaifen                 |                    | gallagher  |
| ICE         | 5      | jingliu                   | yanqing   |           | ruanmei   |                           | gepard             |            |
| ICE         | 4      | misha                     |           | herta     |           | pela                      | mar7th             |            |
| LIGHTENING  | 5      |                           |           | jingyuan  |           | acheron\|kafka            |                    | bailu      |
| LIGHTENING  | 4      | arlan                     | moze      | serval    | tingyun   |                           |                    |            |
| WIND        | 5      | blade                     | feixiao   |           | bronya    | blackswann                |                    | huohuo     |
| WIND        | 4      |                           | danheng   |           |           | sampo                     |                    |            |
| QUANTUM     | 5      |                           | seele     | jade      | sparkle   | silverwolf                | fuxuan             |            |
| QUANTUM     | 4      | xueyi                     |           | qingque   |           |                           |                    | lynx       |
| IMAGINARY   | 5      | danhengil                 | drratio   |           | player3   | welt                      | aventurine         | luocha     |
| IMAGINARY   | 4      |                           | mar7th2   |           | yukong    |                           |                    |            |
<!-- CHARACTER_TABLE_END -->

## Hauptmerkmale
- Lädt automatisch Charakterdaten, CVs, Fähigkeitssets und Relikt-Empfehlungen herunter.
- Verarbeitet und organisiert Daten in versionsspezifische Eingabe-/Ausgabeverzeichnisse.
- Konfiguration der Versionsnummern über die Befehlszeile für jedes neue Update.

## Anforderungen

Stellen Sie sicher, dass Sie Folgendes haben:
- **Python 3.8+** (bestätigen mit `python3 --version`).
- Erforderliche Python-Pakete sind in der `requirements.txt` aufgelistet.

## Installation

1. **Repository klonen:**
   ```bash
   git clone https://github.com/yourusername/hsr-helper.git
   cd hsr-helper
   ```

2. **(Optional) Erstellen und Aktivieren einer virtuellen Umgebung:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Unter Windows: venv\Scriptsctivate
   ```

3. **Abhängigkeiten installieren (derzeit keine zusätzlichen Abhängigkeiten erforderlich):**
   ```bash
   # Derzeit müssen keine Abhängigkeiten installiert werden, aber falls in Zukunft erforderlich:
   # pip install -r requirements.txt
   ```

## Verwendung

### Werkzeug ausführen
   Navigieren Sie zum Verzeichnis `src/` und führen Sie das Hauptskript mit der gewünschten Versionsnummer aus:
   ```bash
   cd src
   python3 main.py --version <version_number> [--skip-download]
   ```

   - Ersetzen Sie `<version_number>` durch die aktuelle Version (z.B. `2.5`).
   - Wenn Sie das Herunterladen der Dateien überspringen möchten, fügen Sie das Flag `--skip-download` hinzu.

   Die Eingabedateien werden in das Verzeichnis `input/{version}` heruntergeladen und die Ausgabe wird im Verzeichnis `output/{version}` gespeichert.

### Anwendungsbeispiele

- Um das Skript mit Version `2.5` auszuführen und die Dateien herunterzuladen:
  ```bash
  python3 main.py --version 2.5
  ```

- Um das Skript mit Version `2.5` auszuführen und das Herunterladen der Dateien zu überspringen:
  ```bash
  python3 main.py --version 2.5 --skip-download
  ```

- Um das Skript mit Version `2.5` auszuführen und die Dateien für bestimmte Sprachen herunterzuladen (z.B. EN und JP):
  ```bash
  python3 main.py --version 2.5 --languages EN JP
  ```

## Beitragen

Wir freuen uns über Beiträge! Sie können:
- Einen Pull-Request für neue Funktionen oder Fehlerbehebungen einreichen.
- Probleme über den Issue-Tracker melden.
- Stellen Sie sicher, dass alle Beiträge Tests und relevante Dokumentation enthalten.

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die Datei [LICENSE](LICENSE) für weitere Informationen.
