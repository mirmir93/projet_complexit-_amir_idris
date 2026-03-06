
import os
import time
from grid import load_grid
from algorithms import greedy_search, astar_search, genetic_search

GRID_DIR = os.path.join(os.path.dirname(__file__), "data")

def afficher_chemin(grid, path, nom):
    path_set = set(path)
    print(f"\n  Chemin {nom} :")
    for y, row in enumerate(grid):
        ligne = ""
        for x, cell in enumerate(row):
            if (x, y) in path_set and cell not in ('S', 'G'):
                ligne += "* "
            else:
                ligne += cell + " "
        print("   " + ligne)

for i in range(1, 4):
    grid, start, goal = load_grid(os.path.join(GRID_DIR, f"grid{i}.txt"))

    print(f"\n--- Grid {i} | depart={start} but={goal} ---")

    t0 = time.time(); path_greedy = greedy_search(grid, start, goal); t1 = time.time()
    print(f"Glouton  : {len(path_greedy)} etapes | {(t1-t0)*1000:.2f} ms")
    afficher_chemin(grid, path_greedy, "Glouton")

    t0 = time.time(); path_astar = astar_search(grid, start, goal); t1 = time.time()
    print(f"A*       : {len(path_astar)} etapes | {(t1-t0)*1000:.2f} ms")
    afficher_chemin(grid, path_astar, "A*")

    t0 = time.time(); path_genetic = genetic_search(grid, start, goal); t1 = time.time()
    print(f"Genetique: {len(path_genetic)} etapes | {(t1-t0)*1000:.2f} ms")
    afficher_chemin(grid, path_genetic, "Genetique")
