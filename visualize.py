import matplotlib.pyplot as plt
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from grid import load_grid
from algorithms import greedy_search, astar_search, genetic_search

GRID_DIR = os.path.join(os.path.dirname(__file__), "data")

def afficher_grille(ax, grid, path, titre):
    path_set = set(path)
    rows = len(grid)
    cols = len(grid[0])

    for y in range(rows):
        for x in range(cols):
            cell = grid[y][x]
            if cell == 'X':
                color = 'black'
            elif cell == 'S':
                color = 'green'
            elif cell == 'G':
                color = 'red'
            elif (x, y) in path_set:
                color = 'lightblue'
            else:
                color = 'white'

            rect = plt.Rectangle([x, rows-1-y], 1, 1, facecolor=color, edgecolor='gray')
            ax.add_patch(rect)

            if cell in ('S', 'G'):
                ax.text(x+0.5, rows-1-y+0.5, cell, ha='center', va='center',
                        fontsize=13, fontweight='bold', color='white')
            elif cell == 'X':
                ax.text(x+0.5, rows-1-y+0.5, 'X', ha='center', va='center',
                        fontsize=11, color='gray')

    for k in range(1, len(path)):
        x0, y0 = path[k-1]
        x1, y1 = path[k]
        mx0, my0 = x0+0.5, rows-1-y0+0.5
        mx1, my1 = x1+0.5, rows-1-y1+0.5
        dx, dy = mx1-mx0, my1-my0
        ax.annotate("", xy=(mx1-dx*0.2, my1-dy*0.2), xytext=(mx0+dx*0.2, my0+dy*0.2),
                    arrowprops=dict(arrowstyle="-|>", color='blue', lw=1.5))

    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    ax.set_aspect('equal')
    ax.set_title(f"{titre} ({len(path)} etapes)")
    ax.axis('off')


for i in range(1, 4):
    grid, start, goal = load_grid(os.path.join(GRID_DIR, f"grid{i}.txt"))
    path_greedy = greedy_search(grid, start, goal)
    path_astar = astar_search(grid, start, goal)
    path_genetic = genetic_search(grid, start, goal)

    fig, axes = plt.subplots(1, 3, figsize=(16, 4))
    fig.suptitle(f"Grid {i}")

    afficher_grille(axes[0], grid, path_greedy, "Glouton")
    afficher_grille(axes[1], grid, path_astar, "A*")
    afficher_grille(axes[2], grid, path_genetic, "Genetique")

    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(__file__), f"grid{i}_result.png"), dpi=100, bbox_inches='tight')

plt.show()

