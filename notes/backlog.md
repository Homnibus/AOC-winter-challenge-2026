# Backlog - Winter Challenge 2026

Backlog Scrum du projet (versionne dans Git).
Chaque item a une priorite et un statut, pour suivre l avancement au fil des commits.

## Statuts

- `todo`: non commence
- `in-progress`: en cours
- `done`: termine
- `blocked`: bloque

## Priorites

- `P0`: critique / immediate
- `P1`: importante
- `P2`: utile
- `P3`: confort

## Backlog items

| ID     | Priorite | Statut      | Item                                                   | Definition of done                                                                            |
| ------ | -------- | ----------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| BL-001 | P0       | in-progress | Gerer les cas gravite sur les ordres `UP`              | Plus de montee non realisable evidente en simulation sur cas cibles + tests de non-regression |
| BL-002 | P0       | todo        | Ajouter test de non-regression input partiel/inattendu | Cas reproduit en test, correction minimale, test vert                                         |
| BL-003 | P1       | todo        | Smoke test de game complete documente                  | Procedure simple dans README + resultat attendu                                               |
| BL-004 | P1       | todo        | Campagne multi-seed pour evaluer winrate               | Script qui lance N seeds et calcule winrate + score moyen                                     |
| BL-005 | P1       | todo        | Rapport de bataille narratif                           | Resume lisible non-technique + bloc metriques (score/issue/seed/erreurs)                      |
| BL-006 | P1       | done        | Unifier la simulation en un seul script configurable   | Un seul script headless avec options bot/seed documentees                                     |
| BL-007 | P2       | todo        | Ciblage energie non contestee                          | Heuristique simple + tests dedies                                                             |
| BL-008 | P2       | todo        | Anti-piege local (cul-de-sac)                          | Detection locale faible cout + fallback deterministe                                          |
| BL-009 | P3       | todo        | Harmoniser structure docs (notes vs docs)              | Decision explicite documentee et migration si necessaire                                      |
| BL-010 | P3       | todo        | Reintroduire un mode viewer web fiable                 | Assets viewer resolves ou procedure claire de lancement                                       |
| BL-011 | P2       | todo        | Historiser plusieurs versions du bot pour duels        | Convention de versions + commande de match vX vs vY                                           |
| BL-012 | P2       | done        | Archiver le starter officiel Python CodinGame          | Fichier de reference versionne pour comparer les evolutions                                   |

## Rituels

1. Debut de session: choisir un item `todo` le plus prioritaire et le passer `in-progress`.
2. Fin de session: mettre a jour statut + ajouter une ligne dans `notes/iteration-log.md`.
3. Toute decision majeure: mettre a jour `notes/project-context.md`.

## Disclaimer IA / mode agent

- Le code de ce depot est majoritairement genere/edite avec IA (mode agent Copilot).
- Toute proposition IA doit etre relue humainement avant merge/push.
- Les tests et simulations servent de garde-fous minimaux, pas de garantie absolue.
