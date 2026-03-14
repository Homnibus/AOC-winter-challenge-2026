# Winter Challenge 2026 - Codingame

Depot de travail pour participer au Winter Challenge 2026.

Ce repo est configure pour developper un bot Python avec un workflow
"iteration courte + tests de non-regression".

## Objectifs

- Garder un historique propre des strategies et versions.
- Faciliter les tests locaux.
- Suivre les idees et ameliorations entre les ligues.

## Structure proposee

- `src/` : code principal du bot
- `tests/` : scripts et cas de test locaux
- `notes/` : observations, hypotheses, post-mortem
- `.github/` : configuration Copilot (instructions, agent, prompts)

## Disclaimer IA

- Ce projet est developpe en grande partie avec IA (mode agent Copilot).
- Chaque changement doit etre valide par revue humaine + tests locaux.

## Workflow conseille

1. Creer une branche pour une idee: `git checkout -b feat/<idee>`
2. Tester localement
3. Commit clair: `git commit -m "feat: <description>"`
4. Fusionner sur `main` quand stable

## Setup Python local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Simulation locale (moteur officiel)

Le depot officiel est clone dans `external/WinterChallenge2026-Exotec`.

Prerequis:

- Java 17
- Maven
- Python disponible en commande `python`

Lancer une simulation locale headless avec rapport de resultat (scores + gagnant):

```powershell
./scripts/run-local-report.ps1
```

Script unique configurable (quel bot contre quel bot):

```powershell
./scripts/run-local-report.ps1 `
	-Player1Cmd 'python ../../src/main.py' `
	-Player1Name 'My Python Bot' `
	-Player2Cmd 'python config/Boss.py' `
	-Player2Name 'Boss Baseline' `
	-Seed '123456'
```

Generer un fichier Python unique pret pour copie/colle sur CodinGame:

```powershell
python ./scripts/build_single_file.py
```

Alternative PowerShell (wrapper):

```powershell
./scripts/build-codingame-singlefile.ps1
```

Fichier genere:

- `dist/codingame_bot.py`

## Commandes qualite

```bash
pytest
ruff check src tests
black --check src tests
```

## Config agent Copilot

- Instructions globales: `.github/copilot-instructions.md`
- Instructions Python: `.github/instructions/codingame-python.instructions.md`
- Instructions tests: `.github/instructions/codingame-tests.instructions.md`
- Agent dedie strategie: `.github/agents/codingame-strategist.agent.md`
- Prompt d iteration: `.github/prompts/challenge-iteration.prompt.md`

## Contexte persistant

- Source de contexte court: `notes/project-context.md`
- Historique d iterations: `notes/iteration-log.md`
- Backlog Scrum priorise: `notes/backlog.md`
- Regle d usage: avant toute modification, lire ces deux fichiers; apres une iteration significative, mettre a jour au moins `notes/project-context.md`.

## Process challenge recommande

1. Completer `notes/challenge-brief-template.md` avec les regles.
2. Implementer le parser tour dans `src/main.py`.
3. Implementer les heuristiques dans `src/strategy.py`.
4. Ajouter un test par bug corrige dans `tests/`.
5. Tenir a jour `notes/iteration-log.md`.

## Commandes utiles

```bash
git status
git add .
git commit -m "chore: update bot"
git log --oneline --decorate --graph
```

## Remote GitHub (optionnel)

```bash
git remote add origin <URL_DU_REPO>
git push -u origin main
```
