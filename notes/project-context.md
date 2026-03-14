# Project Context - Winter Challenge 2026

Ce fichier est la source de verite courte pour conserver le contexte d une session a l autre.
Il doit rester concis et etre mis a jour a chaque changement strategique notable.

## Date de reference

- 2026-03-14

## Etat actuel

- Bot Python en place avec parsing I/O, modele d etat et heuristique simple.
- Reference officielle du starter Python CodinGame archivee dans `notes/codingame-python-starter-reference.py`.
- Strategie actuelle: cibler la source d energie la plus proche avec fallback deterministe.
- Simulateur local officiel branche via PowerShell sur `external/WinterChallenge2026-Exotec`.
- Pipeline qualite local: pytest, ruff, black.
- Backlog Scrum priorise disponible dans `notes/backlog.md` (source de verite plan d action).
- Priorite immediate: iteration strategie sur la gravite avec tests de non-regression.
- Validation locale effectuee: `pytest` OK, `ruff` OK, `black --check` OK.
- Simulation headless avec rapport chiffrable active via `scripts/run-local-report.ps1` (script unique configurable).
- Rapport valide: score bot vs Boss, issue (win/draw/loss), erreurs agents, nombre de frames.
- Generation fichier bot unique disponible via `scripts/build-codingame-singlefile.ps1` -> `dist/codingame_bot.py`.
- Validation effectuee: le fichier unique `dist/codingame_bot.py` gagne aussi en simulation locale headless.

## Architecture active

- `src/main.py`: lecture input Codingame et boucle de tour.
- `src/game_state.py`: modeles (`Point`, `Snakebot`, `GameConfig`, `TurnState`) et parsing.
- `src/strategy.py`: choix des actions par serpent.
- Ces 3 fichiers ont recu une passe de lisibilite/simplicite sans changer la logique de base.
- `tests/test_game_state.py`: parser et extraction de grille.
- `tests/test_strategy.py`: non-regression comportement de base.
- `notes/backlog.md`: backlog strategy (plan de bataille evolutif).

## Decisions prises

- Priorite a la robustesse: toujours produire une action valide (`WAIT` si aucun snake actif).
- Priorite a la simplicite: heuristiques O(n), pas de recherche complexe fragile.
- Priorite au test de non-regression pour chaque bug corrige.

## Limites connues

- Pas d anticipation explicite de gravite/collision future a plus d un tour.
- Cas concret remonte: ordre `UP` parfois non realisable a cause de la gravite, avec perte de tour.
- Pas de coordination avancee multi-snake (roles, repartition energie).
- Pas de modelisation predictive des mouvements adverses.
- Pas de mode viewer web conserve pour le moment (volontaire, priorite au flux headless textuel).

## Prochaines pistes a faible risque

1. Eviter les demi-tours dangereux quand une alternative sure existe.
2. Priorite gravite: detecter/eviter les montees `UP` non realisables.
3. Prioriser les energies non contestees a distance equivalente.
4. Ajouter une regle anti-piege local (eviter cul-de-sac immediate).
5. Ajouter un format de "rapport de bataille" lisible non-technique en sortie des simulations.

## Etape projet en cours

- Phase active: Debut Phase 3 (strategie baseline robuste).
- Critere de sortie de phase: correction du premier axe gravite avec test de non-regression dedie.
- Validation courante: tests renforces (`pytest` 7 passes), lint/format propres.
- Suivi des prochains items: `notes/backlog.md`.

## Checklist update contexte (a chaque iteration)

1. Mettre a jour ce fichier (etat actuel, decisions, limites, prochaine piste).
2. Ajouter une ligne dans `notes/iteration-log.md`.
3. Si bug corrige: ajouter/mettre a jour un test dans `tests/`.
