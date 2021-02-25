import pygame
from pygame.locals import *
import numpy as np 

import constants

# draw the whole screen according to above parameters
def draw_game(screen, grid, myfont):

    screen.fill(constants.CP['back'])

    for i in range(constants.GRID_ORDER):
        for j in range(constants.GRID_ORDER):
            n = grid[i][j]
              
            # padding everything
            rect_x = j * constants.WIDTH // constants.GRID_ORDER + constants.SPACING
            rect_y = i * constants.HEIGHT // constants.GRID_ORDER + constants.SPACING
            rect_w = constants.WIDTH // constants.GRID_ORDER - 2 * constants.SPACING
            rect_h = constants.HEIGHT // constants.GRID_ORDER - 2 * constants.SPACING

            # draw rectangle
            pygame.draw.rect(
                screen, constants.CP[n], 
                pygame.Rect(rect_x, rect_y, rect_w, rect_h), 
                border_radius=8)

            if n == 0:
                n = ""
            text_surface = myfont.render(f"{n}", True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=(rect_x + rect_w/2, rect_y + rect_h/2))

            screen.blit(text_surface, text_rect)

def display(state, score):

    current_state = np.array(state)
    
    pygame.init()
    pygame.display.set_caption(f"2048: Defeating Argha Das, CURRENT SCORE: {score}")

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 42)

    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

    draw_game(screen, current_state, myfont)
    pygame.display.flip()
