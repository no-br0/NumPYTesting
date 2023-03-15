import numpy as np
import Variables as Vars

class GridManager():
    def __init__(self):
        self.grid = np.zeros(Vars.GRID_SIZE, dtype=int)