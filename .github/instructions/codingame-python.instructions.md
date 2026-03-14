---
applyTo: "src/**/*.py"
description: "Use when editing the Codingame Python bot logic, parser, state model, and turn decisions."
---

# Python Bot Instructions

## Architecture cible

Le code dans `src/` doit suivre cette separation:

- Parsing des entrees dans `main.py`.
- Structures d etat dans `game_state.py`.
- Decision strategique dans `strategy.py`.

## Regles de robustesse

- Toujours retourner une action valide meme en cas d entree inattendue.
- Eviter les exceptions non gerees dans la boucle de tour.
- Les fonctions de strategie doivent etre pures quand possible.

## Performance

- Limiter les copies de structures a chaque tour.
- Garder des calculs O(n) par tour sauf besoin explicite.
- Eviter les logs verbeux en production.

## Qualite

- Ajouter des types pour les modeles et fonctions critiques.
- Ajouter un test de non-regression pour tout bug corrige.
- Preferer des heuristiques explicables plutot que des regles opaques.
