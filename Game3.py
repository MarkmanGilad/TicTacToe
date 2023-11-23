# clock & Frame Per Second

import pygame
from Graphics import *
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()


# Main Loop
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # The code


    pygame.display.update()
    clock.tick(FPS)
    

