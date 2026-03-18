# 📓 Notes Personnelles — Projet Heuristiques Robot

Ce notebook regroupe toutes mes notes sur le projet : description de chaque fichier, explication des algorithmes, et exécution du code pour voir les résultats en direct.

---

## 1. `grid.py` — Chargement de la grille

**Fichier original, non modifié.**

Contient `load_grid(file)` qui :
- Ouvre un fichier `.txt` de grille
- Détecte automatiquement `S` (départ) et `G` (arrivée)
- Retourne : `grid` (liste de listes), `start (x,y)`, `goal (x,y)`

> `x` = colonne (gauche → droite), `y` = ligne (haut → bas)

```python
import sys, os
sys.path.insert(0, r'c:\Users\acher\Downloads\ProjetBDMLoptimisation\ProjetBDMLoptimisation')
os.chdir(r'c:\Users\acher\Downloads\ProjetBDMLoptimisation\ProjetBDMLoptimisation')

from grid import load_grid

grid, start, goal = load_grid('data/grid1.txt')
print('Départ :', start)
print('Arrivée :', goal)
print('Grille :')
for row in grid:
    print(' ', ' '.join(row))
```

---

## 2. `algorithms/greedy.py` — Greedy Best-First Search

**Fichier complété** (le squelette faisait juste `return [start]`).

### Ce qui a été ajouté :
- File de priorité (`heapq`) triée par `h(n)` = distance de Manhattan vers le but
- `came_from` : dictionnaire pour mémoriser d'où on vient
- Reconstruction du chemin en remontant `came_from` depuis `G` jusqu'à `S`

### Formule heuristique :
$$h(n) = |x_n - x_{goal}| + |y_n - y_{goal}|$$

### ⚠️ Limite :
Greedy **ne garantit pas** le chemin le plus court. Il ne regarde que l'estimation vers le but, pas le coût déjà parcouru.

```python
from algorithms import greedy_search

path = greedy_search(grid, start, goal)
print(f'Chemin Greedy ({len(path)} étapes) :')
print(path)

# Affichage visuel
path_set = set(path)
for y, row in enumerate(grid):
    line = ''
    for x, cell in enumerate(row):
        if (x, y) in path_set and cell not in ('S', 'G'):
            line += '* '
        else:
            line += cell + ' '
    print(' ', line)
```

---

## 3. `algorithms/astar.py` — A* Search

**Fichier complété** (le squelette retournait `[]`).

### Ce qui a été ajouté :
- File de priorité triée par `f(n) = g(n) + h(n)`
  - `g(n)` = coût réel depuis le départ (nb de cases parcourues)
  - `h(n)` = estimation Manhattan jusqu'au but
- `g_score` : mémorise le meilleur coût connu pour chaque case
- Mise à jour si on trouve un chemin plus court vers une case déjà visitée

### ✅ Avantage :
A* est **optimal** — garantit toujours le chemin le plus court.

```python
from algorithms import astar_search

path = astar_search(grid, start, goal)
print(f'Chemin A* ({len(path)} étapes) :')
print(path)

path_set = set(path)
for y, row in enumerate(grid):
    line = ''
    for x, cell in enumerate(row):
        if (x, y) in path_set and cell not in ('S', 'G'):
            line += '* '
        else:
            line += cell + ' '
    print(' ', line)
```

---

## 4. Comparaison Greedy vs A* sur les 3 grilles

```python
from algorithms import greedy_search, astar_search
from grid import load_grid

results = []
for i in range(1, 4):
    g, s, goal = load_grid(f'data/grid{i}.txt')
    pg = greedy_search(g, s, goal)
    pa = astar_search(g, s, goal)
    results.append((i, len(pg), len(pa)))
    print(f'Grid {i} | Greedy : {len(pg)} étapes | A* : {len(pa)} étapes | Différence : {len(pg)-len(pa)}')

print()
print('→ A* est optimal et trouve toujours le chemin le plus court ou égal à Greedy.')
```

---

## 5. `visualize.py` — Visualisation graphique

**Fichier créé en plus** (pas dans le squelette original).

Utilise `matplotlib` pour afficher les grilles en couleur avec des flèches directionnelles.
Pour chaque grille, 3 sous-graphiques côte à côte : Glouton, A*, Génétique.

| Couleur | Signification |
|---------|---------------|
| Vert | Départ `S` |
| Rouge | Arrivée `G` |
| Bleu clair | Cases du chemin |
| Noir | Obstacle `X` |
| Blanc | Case libre |
| Flèches bleues | Direction du déplacement |

---

## 6. Résumé des fichiers

| Fichier | Statut | Description |
|---------|--------|-------------|
| grid.py | Original | Chargement de la grille, non modifié |
| algorithms/greedy.py | Complété | Algorithme glouton |
| algorithms/astar.py | Complété | Algorithme A* |
| algorithms/genetic.py | Nouveau | Algorithme génétique |
| algorithms/__init__.py | Nouveau | Package Python |
| main.py | Réécrit | Affichage textuel des résultats avec temps |
| visualize.py | Nouveau | Visualisation graphique matplotlib |
| data/grid1-3.txt | Original | Fichiers de grilles |
| README.md | Nouveau | Documentation du projet |

---

## 7. Notes pour la présentation

Plan :
1. Présenter le problème : un robot sur une grille avec des obstacles
2. Expliquer le format des grilles (S, G, X, 0)
3. Algorithme glouton : heuristique de Manhattan, rapide mais pas toujours optimal
4. Algorithme A* : f = g + h, garantit le chemin le plus court
5. Algorithme génétique : chemin = suite de mouvements, amélioré par sélection et mutation
6. Comparaison des résultats sur les 3 grilles
7. Conclusion : quand utiliser l'un ou l'autre ?

---

Points à retenir :
- Manhattan : h(n) = |x - x_but| + |y - y_but|, fonctionne car déplacement en 4 directions uniquement
- Glouton : regarde seulement h(n), rapide mais peut rater l'optimal
- A* : regarde f(n) = g(n) + h(n), garantit le chemin le plus court
- Génétique : chemin = suite de mouvements aléatoires, améliorés par sélection et mutation
- Grid 1 : Glouton = 11 étapes, A* = 9 étapes, Génétique = variable
- Grid 2 et 3 : Glouton et A* = 9 étapes, Génétique = variable

---

Questions probables du jury :

| Question | Réponse |
|----------|---------|
| Pourquoi Manhattan et pas Euclidienne ? | On se déplace en 4 directions seulement, pas en diagonale |
| A* est-il toujours meilleur que le glouton ? | Toujours optimal, mais explore plus de cases donc légèrement plus lent |
| Que se passe-t-il s'il n'y a pas de chemin ? | Les algorithmes retournent une liste vide |
| C'est quoi heapq ? | File de priorité Python, retourne toujours le plus petit élément |
| Pourquoi le génétique est plus lent ? | Il fait 200 générations de 100 individus, soit 20000 évaluations |
| Le génétique trouve-t-il toujours l'optimal ? | Non, il est aléatoire et ne garantit pas le chemin le plus court |
