# Animation

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


pygame.draw.line(surface=main_surf, color=BLACK, start_pos=(10,10), end_pos=(100,100), width=5)
pygame.draw.circle(surface=main_surf, color=GREEN, center= (50,50), radius=20, width=2)
pygame.draw.circle(surface=header_surf, color=RED, center= (150,50), radius=30, width=0)
screen.blit(header_surf, (0,0))
screen.blit(main_surf, (0,100))

# x_img = pygame.image.load("img/x_img.png")
x_img = pygame.image.load("img/space_ship.png")
x_img = pygame.transform.scale(x_img, (40, 40))

# Main Loop
run = True
x1, y1 = 300, 50

while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y =  event.pos #pygame.mouse.get_pos()
            pos = x - 20, y - 100 - 20
            main_surf.blit(x_img,pos)

    header_surf.fill(BLUE)
    header_surf.blit(x_img, (x1,y1))
    x1 = (x1 - 2) % 300
    screen.blit(header_surf, (0,0))
    screen.blit(main_surf, (0,100))
    pygame.display.update()
    clock.tick(FPS)


