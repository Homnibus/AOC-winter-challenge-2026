# Codingame 2026 Workspace Instructions

Objectif: produire un bot Python robuste et iterer vite entre simulation locale et soumission.

## Principes de dev

- Favoriser un code simple, lisible, testable.
- Separer parsing I/O, modele d etat, et logique de decision.
- Eviter les optimisations prematures.
- Ajouter des tests pour chaque regression connue.
- Preserver la compatibilite avec l execution en temps limite de Codingame.

## Contraintes Codingame

- Toujours privilegier une sortie valide plutot qu une strategie complexe fragile.
- Si une information du jeu manque ou est incertaine, appliquer une action de fallback deterministe.
- Chaque tour doit etre calcule en temps borne.
- Eviter les allocations inutiles dans la boucle principale.

## Workflow recommande

1. Capturer les regles et hypotheses dans `notes/`.
2. Implementer une strategie petite et testable dans `src/strategy.py`.
3. Couvrir les cas limites avec `pytest`.
4. Ajouter des tests de non-regression quand un bug est trouve.
5. Maintenir un changelog court des iterations dans `notes/`.

## Contexte persistant obligatoire

- Avant toute proposition de changement: lire `notes/project-context.md`, `notes/iteration-log.md` et `notes/backlog.md`.
- Apres tout changement significatif: mettre a jour `notes/project-context.md`.
- Toute decision strategique doit etre tracee de facon concise dans ce fichier.
- En cas de contexte incomplet ou ambigu, choisir un fallback deterministe et le noter.

## Style Python

- Python 3.11+.
- Typage explicite sur les structures principales.
- Fonctions courtes et nommage clair.
- Aucune dependance runtime inutile pour le bot final.

## Attentes vis-a-vis de l agent

Quand l agent propose une modification:

- Prioriser la correction comportementale et la robustesse.
- Expliquer les compromis (rapidite vs precision strategique).
- Inclure au minimum un test quand c est possible.
- Mentionner les limites restantes et prochaines etapes utiles.
