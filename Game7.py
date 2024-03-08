# User Interface

import pygame
from Graphics import *
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gilad')
clock = pygame.time.Clock()
header_surf = pygame.Surface((H_WIDTH, H_HEIGHT))
main_surf = pygame.Surface((M_WIDTH, M_HEIGHT))
header_surf.fill(BLUE)
main_surf.fill(LIGHTGRAY)


x_img = pygame.image.load("img/x_img.png")
x_img = pygame.transform.scale(x_img, (40, 40))
main_surf.blit(x_img,(0,0))

# Main Loop
run = True
while (run):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            #x,y = pygame.mouse.get_pos()
            x, y = event.pos
            print(x,y)
            x = x - 20
            y = y - 100 - 20

            main_surf.blit(x_img,(x,y))
            # print(events)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                header_surf.fill(GREEN)
            if event.key == pygame.K_RIGHT:
                header_surf.fill(CADETBLUE1)
                

    screen.blit(header_surf, (0,0))
    screen.blit(main_surf, (0,100))
    pygame.display.update()
    clock.tick(FPS)
    

