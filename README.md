# cs-demo-viewer

Personligt hobbyprojekt: et værktøj til at forberede sig før en FACEIT CS2-kamp.

Idéen er at slå modstanderne op via FACEIT Data API, parse deres seneste demoer
på det valgte map og vise, hvor de typisk står og dør, som heatmaps oven på radaren.

## Status

Tidlig fase. Indtil videre findes en lille FACEIT API-klient (`backend/faceit.py`).

## Planlagt

- Hent kamp og fjendtlige spillere fra FACEIT
- Parse demoer med `demoparser2`
- Aggreger positioner pr. spiller og map
- Web-UI med heatmap

## Opsætning

```
pip install -r requirements.txt
cp .env.example .env   # udfyld FACEIT_API_KEY
```

API-nøglen må aldrig committes.

Dette projekt er ikke tilknyttet eller godkendt af FACEIT.
