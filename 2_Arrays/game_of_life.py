"""
Game is played over a specific period of time with each turn creating a new generation, based on current configuration

1. If a cell is alive and has 2 or 3 live neighbours, cell continues to remain alive in next gen
2. A living cell that has no live neighbours or a single neighbour dies from isolation
3. A living cell that has four or more live neighbours dies from overpopulation.
4. A dead cell with exactly 3 live neighbours results in a birth and becomes alive in next gen.
"""

from Life_Grid_ADT import LifeGrid

INITIAL_CONNFIG = [(1, 2), (2, 1), (2, 2), (2, 3)]
GRID_WIDTH = 5
GRID_HEIGHT = 5
NUM_GENS = 8

def main():
    grid = LifeGrid(GRID_HEIGHT, GRID_HEIGHT)
    grid.configure(INITIAL_CONNFIG)

    draw(grid)
    for i in range(NUM_GENS):
        evolve(grid)
        draw(grid)

def evolve(grid):
    live_cells = list()
    for i in range(grid.num_rows()):
        for j in range(grid.num_cols()):
            neighbours = grid.num_live_neighbours((i, j))
            if (neighbours == 2 and grid.is_live_cell((i, j))) or \
                    (neighbours == 3):
                live_cells.append((i, j))
    grid.configure(live_cells)

def draw(grid):
    for i in range(grid.num_rows()):
        print('|', end='')
        for j in range(grid.num_cols()):
            if grid[i, j] == 0:
                print('.', end='|')
            else:
                print('@', end='|')
        print("\n==", '=='*GRID_HEIGHT, sep='')
    print('\n\n')

main()