from GridManager import GridManager
from ScreenManager import ScreenManager

import numpy as np
import Variables as Vars
import pygame

pygame.init()

pygame.display.set_caption("Game Of Wonderment")

screen_manager = ScreenManager()
grid_manager = GridManager()

COUNTER = 0
COUNTER_LIMIT = 20


#grid_manager.grid[::16] = 1
#grid_manager.grid[:,::16] = 1
#grid_manager.grid[::2] = 1
#grid_manager.grid[1:4,1:4] = 1

print(grid_manager.grid)



def display_grid():
    screen_manager.draw_grid(grid_manager.grid)

#print(grid_manager.grid[grid_manager.grid > 0])

def handle_mouse_event():
    pos = pygame.mouse.get_pos()

    i = pos[0] // Vars.CELL_SIZE[0]
    j = pos[1] // Vars.CELL_SIZE[1]

    if grid_manager.grid[i,j] == 0:
        grid_manager.grid[i,j] = 1
    else:
        grid_manager.grid[i,j] = 0

    display_grid()

if __name__ == "__main__":
    clock = pygame.time.Clock()
    simulating = False
    display_grid()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                handle_mouse_event()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    if simulating:
                        simulating = False
                    else:
                        simulating = True
                    print('simulating: ',simulating)
                elif event.key == pygame.K_c:
                    grid_manager.reset_grid()
                    display_grid()

        if simulating:
            if COUNTER == COUNTER_LIMIT:
                grid_manager.default_step()
                display_grid()

        pygame.display.update()
        if COUNTER < COUNTER_LIMIT:
            COUNTER += 1
        else:
            COUNTER = 0
        
        clock.tick(Vars.FPS)

