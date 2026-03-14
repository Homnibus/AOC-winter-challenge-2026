# Winter Challenge 2026 - Codingame

Depot de travail pour participer au Winter Challenge 2026.

## Objectifs

- Garder un historique propre des strategies et versions.
- Faciliter les tests locaux.
- Suivre les idees et ameliorations entre les ligues.

## Structure proposee

- `src/` : code principal du bot
- `tests/` : scripts et cas de test locaux
- `notes/` : observations, hypotheses, post-mortem

## Workflow conseille

1. Creer une branche pour une idee: `git checkout -b feat/<idee>`
2. Tester localement
3. Commit clair: `git commit -m "feat: <description>"`
4. Fusionner sur `main` quand stable

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
