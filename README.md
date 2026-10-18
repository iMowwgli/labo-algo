# labo-algo

Révisions d'algorithmique S3 (EPITA) : arbres généraux en DFS / BFS et B-arbres.

## Contenu

| Dossier | Quoi |
| --- | --- |
| `arbres-generaux/` | 14 exos (18 fonctions) sur `Tree` et `TreeAsBin`, avec un testeur automatique et les corrigés |
| `fiche/` | Fiche patterns en LaTeX (PDF prêt à imprimer + source) |
| `btree-suppression/` | Page interactive : suppression dans un B-arbre pas à pas, à la descente ou à la remontée, avec mode entraînement |

## Lancer les exos

Les modules du cours (`algo_py/` : `tree.py`, `treeasbin.py`, `queue.py`…) ne sont pas inclus.
Copie ton dossier `algo_py` dans `arbres-generaux/`, puis :

```bash
cd arbres-generaux
python3 entrainement.py      # teste tout
python3 entrainement.py 5    # teste seulement l'exo 5
python3 tests.py solutions   # vérifie les corrigés
```

Règles comme à l'exam : uniquement `len`, `range`, `min`, `max`, `abs` et `Queue`.

## Page B-arbre

Ouvre `btree-suppression/index.html` dans un navigateur (aucune installation).

## Fiche

```bash
cd fiche && pdflatex fiche_arbres.tex
```
