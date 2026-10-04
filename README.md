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