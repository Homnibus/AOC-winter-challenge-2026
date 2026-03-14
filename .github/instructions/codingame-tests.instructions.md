---
applyTo: "tests/**/*.py"
description: "Use when creating or updating tests for Codingame bot behavior and regressions."
---

# Test Instructions

## Priorites de test

- Cas nominal de lecture d etat et action attendue.
- Cas limites: liste vide, valeurs extremas, donnees partielles.
- Non-regression: scenario reintroduisant un bug deja corrige.

## Bonnes pratiques

- Tests rapides et deterministes.
- Un nom de test explicite sur le comportement observe.
- Fixtures legers pour les etats de jeu repetes.

## Focus challenge

Quand un echec apparait en ligue:

1. Reproduire localement via test.
2. Corriger minimalement la logique.
3. Garder le test pour eviter la rechute.
