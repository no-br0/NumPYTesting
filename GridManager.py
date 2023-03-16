import numpy as np
import Variables as Vars

class GridManager():
    def __init__(self):
        self.grid = np.zeros(Vars.GRID_SIZE, dtype=int)

    def reset_grid(self):
        self.grid = np.zeros(Vars.GRID_SIZE, dtype=int)

    def default_step(self):
        new_grid = self.grid.copy()
        for col in range(Vars.GRID_SIZE[0]):
            for row in range(Vars.GRID_SIZE[1]):
                sum_area = np.sum(self.grid[max((col-1),0):min((col+2), Vars.GRID_SIZE[0]),max((row-1),0):min((row+2), Vars.GRID_SIZE[1])]) - self.grid[col,row]

                print(f"({col},{row})")
                print(self.grid[max((col-1),0):min((col+2), Vars.GRID_SIZE[0]),max((row-1),0):min((row+2), Vars.GRID_SIZE[1])])
                print(f'sum_area: {sum_area}')
                print("\n")

                if self.grid[col,row] == 1:
                    if sum_area == 3:
                        new_grid[col,row] = 2
                    elif sum_area > 3 or sum_area < 2:
                        new_grid[col,row] = 0
                elif self.grid[col,row] == 0:
                    if sum_area == 3:
                        new_grid[col,row] = 1
                elif self.grid[col,row] == 2:
                    if sum_area == 7:
                        new_grid[col,row] = 1
                    
        
        self.grid = new_grid