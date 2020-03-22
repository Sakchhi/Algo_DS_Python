"""
LifeGrid ADT represents and stores the area in Game of Life that contains organisms
Grid contains rectangular grouping of cells of finite size
Individual cells can be alive or dead

LifeGrid(nrows, ncols)
num_rows(), num_cols()
configure(coord_list): Configures the grid for evolving the next generation. All remaining cells are cleared
clear_cell(row, col), set_cell(row, col), is_live_cell(row, col), num_live_neighbours(row, col)
"""
from Array2d_ADT import Array2D

class LifeGrid:
    DEAD_CELL = 0
    LIVE_CELL = 1

    def __init__(self, nrows, ncols):
        self._life_grid = Array2D(nrows, ncols)
        self.configure(list())

    def num_rows(self):
        return self._life_grid.num_rows()

    def num_cols(self):
        return self._life_grid.num_cols()

    def configure(self, coord_list):
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                self.clear_cell((i, j))
        for coord in coord_list:
            self._life_grid[coord[0], coord[1]] = LifeGrid.LIVE_CELL

    def __getitem__(self, tuple_idx):
        return self._life_grid[tuple_idx[0], tuple_idx[1]]

    def __setitem__(self, tuple_idx, value):
        self._life_grid[tuple_idx[0], tuple_idx[1]] = value

    def clear_cell(self, tuple_idx):
        row = tuple_idx[0]
        col = tuple_idx[1]
        self._life_grid[row,col] = LifeGrid.DEAD_CELL

    def set_cell(self, tuple_idx):
        row = tuple_idx[0]
        col = tuple_idx[1]
        self._life_grid[row,col] = LifeGrid.LIVE_CELL

    def is_live_cell(self, tuple_idx):
        row = tuple_idx[0]
        col = tuple_idx[1]
        return self._life_grid[row, col] == LifeGrid.LIVE_CELL

    def num_live_neighbours(self, tuple_idx):
        row = tuple_idx[0]
        col = tuple_idx[1]
        live = 0
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    # print('inside live try for ({},{})'.format(i,j))
                    live += self._life_grid[row+i, col+j]
                except:
                    pass
        live = live - self._life_grid[row, col]
        # print('({}, {} ==> {}'.format(row, col, live))
        return live
