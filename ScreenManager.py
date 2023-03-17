import pygame
import numpy as np
import Variables as Vars
from Variables import GRID_SIZE, CELL_SIZE
from Colors import DEAD, MUSHROOM, GRASS

class ScreenManager():
    def __init__(self):
        self.screen = pygame.display.set_mode(Vars.WINDOW_SIZE)

    def draw_grid(self, grid):
        self.screen.fill(DEAD)

        for col in range(GRID_SIZE[0]):
            for row in range(GRID_SIZE[1]):
                rect = pygame.Rect(col * CELL_SIZE[0], row * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1])
                if grid[col,row] == 0:
                    pygame.draw.rect(self.screen, DEAD, rect)
                elif grid[col,row] == 1:
                    pygame.draw.rect(self.screen, MUSHROOM, rect)
                elif grid[col,row] == 2:
                    pygame.draw.rect(self.screen, GRASS, rect)


        #pygame.display.update()
