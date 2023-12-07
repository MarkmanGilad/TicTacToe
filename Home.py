# draw shapes

import pygame
from Graphics import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Home')
clock = pygame.time.Clock()

screen.fill(LIGHTGRAY)

# code for Paint Home

# Main Loop
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.update()
    clock.tick(FPS)
    
