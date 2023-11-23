# surfaces & colors
# https://www.pygame.org/docs/ref/color_list.html

import pygame
from Graphics import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
header_surf = pygame.Surface((H_WIDTH, H_HEIGHT))
main_surf = pygame.Surface((M_WIDTH, M_HEIGHT))
header_surf.fill(BLUE)
main_surf.fill(LIGHTGRAY)

screen.blit(header_surf, (0,0))
screen.blit(main_surf, (0,100))


# Main Loop
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()
    clock.tick(FPS)
    

