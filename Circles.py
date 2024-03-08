# User Interface

import pygame
from Graphics import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Gilad')
clock = pygame.time.Clock()
screen.fill(WHITE)
color = BLUE
# Main Loop
run = True
while (run):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print(x,y)
            pygame.draw.circle(surface=screen, color=color, center= (x,y), radius=10, width=0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pass
            if event.key == pygame.K_2:
                pass

    pygame.display.update()
    clock.tick(FPS)
    

