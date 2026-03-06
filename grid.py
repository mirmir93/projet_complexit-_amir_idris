
def load_grid(file):
    grid=[]
    start=None
    goal=None

    with open(file) as f:
        for y,line in enumerate(f):
            row=line.strip().split()
            for x,val in enumerate(row):
                if val=="S":
                    start=(x,y)
                if val=="G":
                    goal=(x,y)
            grid.append(row)

    return grid,start,goal

def get_voisins(grid, pos):
    x, y = pos
    voisins = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] != 'X':
            voisins.append((nx, ny))
    return voisins
