# Unit Converter

A simple Python application for converting units of distance, weight, and temperature.

The project is developed as part of a CI/CD practice project using GitHub Actions.

## Features

- Kilometer ↔ Meter
- Kilogram ↔ Gram
- Celsius ↔ Fahrenheit
- Automated tests with pytest

## Pipeline-Architektur

| Job | Zweck | Trigger / Bedingung | needs | Environment | Artifact |
|---|---|---|---|---|---|
| `test` | Abhängigkeiten installieren, Tests ausführen, ZIP-Paket erstellen und als Artifact hochladen | `push` und `pull_request` | – | – | `unit-converter-package` |
| `deploy` | Artifact herunterladen und automatisiert ein GitHub Release erstellen | Nur auf `main` und nur nach erfolgreichen Tests | `test` | `production` | `unit-converter-package` |

## Trigger

Die Pipeline wird bei folgenden Ereignissen gestartet:

- `push`
- `pull_request`

Der Job `deploy` wird nur auf dem Branch `main` und nur nach einem erfolgreichen `test`-Job ausgeführt.

## Secrets und Environment

Die Pipeline verwendet folgende Konfiguration:

- Secret: `DEPLOY_TOKEN`
- Variable: `DEPLOY_TARGET`
- Environment: `production`

Die Werte von Secrets werden nicht im Repository gespeichert oder in den Logs ausgegeben.

Das Environment `production` ist geschützt und benötigt vor dem Deployment eine Freigabe.

## Deployment

Nach erfolgreichen Tests wird die Anwendung als `unit-converter.zip` verpackt und als Artifact gespeichert.

Der Job `deploy` lädt dieses Artifact herunter und erstellt automatisch ein GitHub Release. Die ZIP-Datei wird dem Release als Asset hinzugefügt.

## Lokal ausführen

Virtuelle Umgebung erstellen:

```powershell
python -m venv .venv
```

Virtuelle Umgebung aktivieren:

```powershell
.venv\Scripts\Activate.ps1
```

Abhängigkeiten installieren:

```powershell
python -m pip install -r requirements.txt
```

Tests ausführen:

```powershell
python -m pytest -v
```

## Debugging Challenge

Im Rahmen der Abschluss-Challenge wurde eine absichtlich fehlerhafte Pipeline analysiert und repariert.

| # | Symptom / Risiko | Ursache | Fix |
|---|---|---|---|
| 1 | Python 3.1 wurde statt Python 3.10 gesucht | `python-version: 3.10` war nicht als String angegeben | Python-Version in Anführungszeichen setzen: `"3.10"` |
| 2 | `build/app.zip` war im Release-Job nicht vorhanden | Jeder Job läuft auf einem eigenen Runner und das Artifact wurde nicht heruntergeladen | Artifact mit `actions/download-artifact@v4` im nachfolgenden Job herunterladen |
| 3 | Dependency-Datei wurde nicht gefunden | Falscher Dateiname `requirement.txt` | Richtigen Dateinamen `requirements.txt` verwenden |
| 4 | Tests liefen vor der Installation der Dependencies | Falsche Reihenfolge der Steps | Dependencies vor den Tests installieren |
| 5 | Deployment lief trotz fehlgeschlagener Tests | `needs: test` fehlte | `needs: test` zum Deployment-Job hinzufügen |
| 6 | Deployment konnte auch außerhalb von `main` ausgeführt werden | Branch-Bedingung fehlte | `if: github.ref == 'refs/heads/main'` hinzufügen |

Nach der Behebung aller Fehler läuft die Pipeline erfolgreich durch.