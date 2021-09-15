# Project Weerstation ESP Test Scripts

Dit is de GitHub repo voor alle 'test-scripts' van de ESP-01.

Het doel van de scripts is om een simpel HTTP GET request to sturen naar of [de zelfgemaakt api](https://github.com/MtL3/WeatherStationExpressServer/tree/develop), of naar een ander endpoint zoals [reqbin](https://reqbin.com/req/nfilsyk5/get-request-example).

Boven elk scripts in de root directory staat een comment van het verschil met de vorige versie en welke output het geeft.

## Reqbin

Reqbin is een simpele service service die met anderstaand request:

```bash
GET /echo/get/json HTTP/1.1
Host: reqbin.com
Accept: */*
```

dit zou moeten returnen:

```bash
{"success":"true"}
```

(Dit gebeurt niet)

## Setup

Deze repo maakt gebruik van [python venv](https://docs.python.org/3/library/venv.html).

### Venv maken

Om de venv te maken kan je '_Scripts/Create venv.bat_' starten of onderstaand command runnen in de root directory:

```bash
py -m venv .venv
```

### Requirements downloaden

Om de requirements te downloaden in de venv kan je '_Scripts/Update Requirements.bat_' starten, of onderstaand command runnen in de root venv:

```bash
pip install -r requirements.txt
```

### Programma's starten

Om python files te starten kun je in de venv in visual studio code het programma runnen via het command:

```bash
py [bestand].py
```

Een andere manier om scripts met de venv te runnen is om het script '_Scripts/Start Program in Venv.bat_' te runnen, deze zal vragen om de naam van het script in de root directory.
