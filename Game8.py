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

x_img = pygame.image.load("img/space_ship.png")
x_img = pygame.transform.scale(x_img, (40, 40))

# Main Loop
run = True
x1, y1 = 300, 50
x2, y2 = 0, 100

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
    
    # main_surf.blit(x_img, (x2,y2))
    # x2 = (x2 + 2) % 300
    
    
    screen.blit(header_surf, (0,0))
    screen.blit(main_surf, (0,100))
    pygame.display.update()
    clock.tick(FPS)


