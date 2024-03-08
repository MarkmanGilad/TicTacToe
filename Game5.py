# draw shapes

import pygame
from Graphics import *
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
header_surf = pygame.Surface((H_WIDTH, H_HEIGHT))
main_surf = pygame.Surface((M_WIDTH, M_HEIGHT))
header_surf.fill(BLUE)
main_surf.fill(LIGHTGRAY)
myColor = BLACK
pygame.draw.line(surface=main_surf, color=myColor, start_pos=(10,10), end_pos=(100,100), width=5)
myColor = RED
pygame.draw.circle(surface=main_surf, color=myColor, center= (150,150), radius=80, width=5)
pygame.draw.circle(surface=header_surf, color=RED, center= (0,0), radius=30, width=0)
pygame.draw.rect(surface=main_surf, color=GREEN,rect=(50,20,150,30),width=2 )
pygame.draw.ellipse(surface=main_surf, color=RED,rect=(50,20,150,40),width=3)
pygame.draw.polygon(surface=main_surf,color=BLUE,points=[(30,250), (190, 250), (80,300)],width=3)

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
    

