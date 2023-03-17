import numpy as np
import Variables as Vars
from Life import Dead, Mushroom, Grass

class GridManager():
    def __init__(self):
        self.grid = np.zeros(Vars.GRID_SIZE, dtype=int)

    def reset_grid(self):
        self.grid = np.zeros(Vars.GRID_SIZE, dtype=int)

    def default_step(self):
        new_grid = self.grid.copy()
        for col in range(Vars.GRID_SIZE[0]):
            for row in range(Vars.GRID_SIZE[1]):
                sum_area = np.sum(self.grid[max((col-1),0):min((col+2), Vars.GRID_SIZE[1]),max((row-1),0):min((row+2), Vars.GRID_SIZE[0])]) - self.grid[col,row]

                #print(f"({col},{row})")
                #print(self.grid[max((col-1),0):min((col+2), Vars.GRID_SIZE[0]),max((row-1),0):min((row+2), Vars.GRID_SIZE[1])])
                #print(f'sum_area: {sum_area}')
                #print("\n")



                #Makes space ships easily
                #if self.grid[col,row] == Mushroom:
                #    if sum_area == 5 or sum_area == 7:
                #        new_grid[col,row] = Grass
                #    elif (sum_area > 3 or sum_area < 2) and sum_area <= 10:
                #        new_grid[col,row] = Dead
                #elif self.grid[col,row] == Dead:
                #    if sum_area == 3 or sum_area >= 10:
                #        new_grid[col,row] = Mushroom
                #elif self.grid[col,row] == Grass:
                #    if sum_area == 7:
                #        new_grid[col,row] = Mushroom


                #
                #if self.grid[col,row] == Dead:
                #    if sum_area == 3 or sum_area == 10:
                #        new_grid[col,row] = Mushroom
                #elif self.grid[col,row] == Mushroom:
                #    if (sum_area > 3 and sum_area < 7) or sum_area <= 1:
                #        new_grid[col,row] = Dead
                #elif self.grid[col,row] == Grass:
                #    pass

                #if self.grid[col,row] == Dead:
                #    if sum_area == 3 or sum_area == 4 or sum_area == 5:
                #        new_grid[col,row] = Mushroom
                #elif self.grid[col,row] == Mushroom:
                #    if  (sum_area < 3 or sum_area > 4):
                #        new_grid[col,row] = Dead
                #elif self.grid[col,row] == Grass:
                #    pass

                if self.grid[col,row] == Dead:
                    if sum_area == 3 or sum_area == 4 or sum_area == 5:
                        new_grid[col,row] = Mushroom
                elif self.grid[col,row] == Mushroom:
                    if  (sum_area < 3 or sum_area > 4):
                        new_grid[col,row] = Dead
                elif self.grid[col,row] == Grass:
                    pass
                    
        
        self.grid[:] = new_grid[:]