# PR Proposal v0 - Setup complet + baseline jouable

## Titre propose

chore(setup): finalize local simulation workflow and submission bundle, add baseline regression coverage

## Objectif

Figer une premiere base propre et reproductible:

- environnement local valide (tests + lint + format)
- simulation locale exploitable avec rapport chiffrable
- generation d un fichier Python unique pour soumission CodinGame
- socle de tests de non-regression renforce
- contexte projet persistant et backlog strategique partages

## Portee

### Infrastructure / workflow

- Ajout des scripts de simulation locale et rapport headless.
- Ajout du builder single-file pour soumission.
- Documentation README et notes harmonisees.

### Installation / simulation (point explicitement couvre)

- Integration du moteur officiel local dans `external/WinterChallenge2026-Exotec`.
- Scripts PowerShell avec bootstrap Java/Maven automatique quand necessaire.
- Un mode de run unique documente:
  - `run-local-report.ps1`: mode headless configurable (bot vs boss, bot vs bot, seed), avec resultat chiffrable

### Bot Python

- Parser/etat/strategie baseline conserves (deterministes).
- Aucune complexification risquee de strategie.
- Renforcement des tests de robustesse.

### Gestion du contexte

- Contexte persistant + iteration log + backlog strategy mis a jour.
- Priorite explicite ajoutee: gestion des cas gravite (montee non realisable).

## Changements principaux

1. Setup et scripts

- `scripts/run-local-report.ps1`
- `scripts/build_single_file.py`
- `scripts/build-codingame-singlefile.ps1`

2. Bot et tests

- `src/game_state.py`
- `src/main.py`
- `src/strategy.py`
- `tests/test_game_state.py`
- `tests/test_strategy.py`

3. Documentation / contexte

- `README.md`
- `notes/project-context.md`
- `notes/iteration-log.md`
- `notes/backlog.md`

4. Hygiene git

- `.gitignore` (ignore `*.egg-info/` et `notes/reports/`)

## Validation executee

- `pytest`: 7 passed
- `ruff check src tests scripts`: passed
- `black --check src tests scripts`: passed
- `powershell -ExecutionPolicy Bypass -File ./scripts/run-local-report.ps1`: run OK, rapport genere
- `powershell -ExecutionPolicy Bypass -File ./scripts/build-codingame-singlefile.ps1`: generation OK

## Impact produit

- Le bot joue une partie locale complete et retourne un score exploitable.
- Le fichier soumission est genere automatiquement (`dist/codingame_bot.py`).
- Le socle est pret pour les iterations strategie avec guardrails de qualite.

## Risques connus

- La strategie n integre pas encore la prediction de gravite (point prioritaire de la prochaine iteration).
- Les scores single-run dependent du seed, pas encore de benchmark multi-seed.
- Les rapports de simulation sont encore techniques (version "rapport de bataille" narrative a faire).
- Le mode viewer web est reporte a plus tard (priorite basse volontaire).

## Review checklist (tech lead)

1. Robustesse I/O:

- verifier que `src/main.py` gere bien les cas de fin de flux.

2. Determinisme/fallback:

- verifier que `src/strategy.py` produit toujours une action valide.

3. Qualite:

- confirmer la couverture minimale des regressions critiques.

4. Workflow local:

- valider scripts PowerShell sur machine propre (Java/Maven absent au depart).

5. Submission:

- verifier que le contenu de `dist/codingame_bot.py` reste coherent avec `src/`.

## Commentaires attendus

- Priorisation precise pour la prochaine PR strategie (gravite d abord).
- Niveau de detail souhaite pour le futur "rapport de bataille".
- Politique de commit des artefacts (garder ou non les rapports d execution).
- Decision structure docs (`notes/` conserve ou migration `docs/` a planifier).
