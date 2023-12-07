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

screen.blit(header_surf, (0,0))
screen.blit(main_surf, (0,100))

space_ship1 = pygame.image.load("img/space_ship.png")
space_ship1 = pygame.transform.scale(space_ship1, (40, 40))

space_ship2 = pygame.image.load("img/space_ship.png")
space_ship2 = pygame.transform.scale(space_ship2, (40, 40))


run = True
x1, y1 = 0, 50
x2, y2 = 50, 100

while (run):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    header_surf.fill(BLUE)

    header_surf.blit(space_ship1, (x1,y1))
    x1 = (x1 + 2) % 300

    # main_surf.blit(space_ship2, (x2,y2))
    # y2 = (y2 + 2) % 300

    screen.blit(header_surf, (0,0))
    screen.blit(main_surf, (0,100))
    pygame.display.update()
    clock.tick(FPS)


