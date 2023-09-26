import numpy as np

class GameOfLifeGrid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = np.zeros((rows, cols), dtype=int)

    def get_cell(self, row, col):
        return self.grid[row][col]

    def toggle_cell(self, row, col):
        self.grid[row][col] = 1 - self.grid[row][col]

    def get_neighbors(self, row, col):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row, new_col = row + i, col + j
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    neighbors.append(self.grid[new_row][new_col])
        return neighbors

    def next_generation(self):
        new_grid = np.zeros((self.rows, self.cols), dtype=int)
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                neighbors = self.get_neighbors(row, col)
                live_neighbors = sum(neighbors)
                if cell == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[row][col] = 0
                    else:
                        new_grid[row][col] = 1
                else:
                    if live_neighbors == 3:
                        new_grid[row][col] = 1
        self.grid = new_grid
