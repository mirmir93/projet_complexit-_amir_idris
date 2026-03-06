import random

MOVES = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # haut, bas, gauche, droite

def est_valide(x, y, grid):
    return 0 <= y < len(grid) and 0 <= x < len(grid[y]) and grid[y][x] != 'X'

def evaluer(individu, grid, start, goal):
    x, y = start
    cases_visitees = {(x, y)}
    for dx, dy in individu:
        nx, ny = x + dx, y + dy
        if est_valide(nx, ny, grid):
            x, y = nx, ny
        if (x, y) == goal:
            break
    dist = abs(x - goal[0]) + abs(y - goal[1])
    penalite = len(cases_visitees - {goal})
    return dist + penalite * 0.1

def simuler_chemin(individu, grid, start, goal):
    x, y = start
    chemin = [(x, y)]
    for dx, dy in individu:
        nx, ny = x + dx, y + dy
        if est_valide(nx, ny, grid):
            x, y = nx, ny
        chemin.append((x, y))
        if (x, y) == goal:
            break
    return chemin

def selectionner(population, scores):
    total = sum(1 / (s + 0.01) for s in scores)
    r = random.uniform(0, total)
    cumul = 0
    for ind, s in zip(population, scores):
        cumul += 1 / (s + 0.01)
        if cumul >= r:
            return ind
    return population[0]

def croiser(parent1, parent2):
    point = random.randint(1, len(parent1) - 1)
    return parent1[:point] + parent2[point:]

def muter(individu, taux=0.1):
    return [random.choice(MOVES) if random.random() < taux else m for m in individu]

def genetic_search(grid, start, goal, taille_pop=100, generations=200, taille_ind=30):
    population = [[random.choice(MOVES) for _ in range(taille_ind)] for _ in range(taille_pop)]

    meilleur = None
    meilleur_score = float('inf')

    for _ in range(generations):
        scores = [evaluer(ind, grid, start, goal) for ind in population]

        for ind, s in zip(population, scores):
            if s < meilleur_score:
                meilleur_score = s
                meilleur = ind

        if meilleur_score == 0:
            break

        nouvelle_pop = []
        for _ in range(taille_pop):
            p1 = selectionner(population, scores)
            p2 = selectionner(population, scores)
            enfant = croiser(p1, p2)
            enfant = muter(enfant)
            nouvelle_pop.append(enfant)
        population = nouvelle_pop

    if meilleur is None:
        return []
    return simuler_chemin(meilleur, grid, start, goal)
