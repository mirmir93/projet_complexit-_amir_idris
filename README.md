# Projet Heuristiques Robot

Ce projet implémente deux algorithmes de recherche de chemin pour un robot sur une grille 2D : l'algorithme glouton et A*.

## Lancer le projet

    python main.py        # affiche les résultats dans le terminal
    python visualize.py   # affiche les chemins graphiquement

Prérequis : Python et matplotlib (pip install matplotlib)

## Organisation des fichiers

- main.py : lance les deux algorithmes sur les 3 grilles et affiche les résultats
- visualize.py : visualisation graphique avec matplotlib
- grid.py : lit une grille depuis un fichier .txt
- algorithms/greedy.py : algorithme glouton
- algorithms/astar.py : algorithme A*
- data/ : les 3 fichiers de grilles (grid1.txt, grid2.txt, grid3.txt)

## Format des grilles

Chaque case peut être : S (départ), G (but), 0 (libre), X (obstacle).

Exemple :

    S 0 0 0 X 0
    0 X 0 0 X 0
    0 X 0 0 0 0
    0 0 0 X 0 G

## Résultats obtenus

Grille 1 : Glouton = 11 étapes (< 1 ms), A* = 9 étapes (< 1 ms), Génétique = ~26 étapes (~870 ms)
Grille 2 : Glouton = 9 étapes  (< 1 ms), A* = 9 étapes (< 1 ms), Génétique = ~17 étapes (~1050 ms)
Grille 3 : Glouton = 9 étapes  (< 1 ms), A* = 9 étapes (< 1 ms), Génétique = ~27 étapes (~950 ms)

Les temps pour Glouton et A* sont négligeables (moins d'un milliseconde sur ces petites grilles).
Le génétique est bien plus lent car il fait 200 générations avec une population de 100 individus.
Les étapes du génétique varient à chaque exécution à cause de l'aléatoire.

Le génétique atteint toujours le but mais ne garantit pas le chemin le plus court car il est basé sur des opérations aléatoires (mutation, croisement).

## Questions d'analyse

Pourquoi le glouton ne garantit pas toujours l'optimal ?

Le glouton choisit à chaque étape la case qui semble la plus proche du but, sans tenir compte du chemin déjà parcouru. Il peut donc emprunter une direction qui paraît bonne au début mais qui donne un chemin plus long au final.

Pourquoi A* est plus efficace ?

A* combine le coût réel depuis le départ (g) et une estimation vers le but (h). Il explore d'abord les chemins les plus prometteurs et garantit de trouver le plus court, tant que l'heuristique ne surestime pas la distance réelle.

Avantages et inconvénients de l'algorithme génétique ?

Avantage : il peut trouver des solutions sur des problèmes complexes où les autres algorithmes ne fonctionnent pas bien.
Inconvénient : les résultats changent à chaque exécution, il ne garantit pas l'optimalité, et il faut régler plusieurs paramètres comme la taille de la population ou le taux de mutation.
