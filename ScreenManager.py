import pygame
import numpy as np
import Variables as Vars
from Variables import GRID_SIZE, CELL_SIZE
from Colors import DEAD, MUSHROOM

class ScreenManager():
    def __init__(self):
        self.screen = pygame.display.set_mode(Vars.WINDOW_SIZE)

    def draw_grid(self, grid):
        self.screen.fill(DEAD)

        for i in range(GRID_SIZE[0]):
            for j in range(GRID_SIZE[1]):
                rect = pygame.Rect(i * CELL_SIZE[0], j * CELL_SIZE[1], CELL_SIZE[0], CELL_SIZE[1])
                if grid[i,j] == 1:
                    pygame.draw.rect(self.screen, MUSHROOM, rect)
                else:
                    pygame.draw.rect(self.screen, DEAD, rect, 1)

        #pygame.display.update()
