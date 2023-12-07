# draw shapes

import pygame
from Graphics import *
pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Home')
clock = pygame.time.Clock()

screen.fill(LIGHTGRAY)

# code for Paint Home

pygame.draw.line(surface=screen, color=BLACK, start_pos=(300,400), end_pos=(100,100), width=5)
pygame.draw.circle(surface=screen, color=GREEN, center= (150,150), radius=80, width=5)
pygame.draw.circle(surface=screen, color=RED, center= (100,1000), radius=30, width=0)
pygame.draw.rect(surface=screen, color=GREEN,rect=(50,20,150,30),width=2 )
pygame.draw.ellipse(surface=screen, color=RED,rect=(50,20,150,40),width=3)
pygame.draw.polygon(surface=screen,color=BLUE,points=[(430,250), (190, 250), (80,300)],width=3)



# Main Loop
run = True
while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        

    pygame.display.update()
    clock.tick(FPS)
    
