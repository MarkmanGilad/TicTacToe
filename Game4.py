# surfaces & colors
# https://www.pygame.org/docs/ref/color_list.html

import pygame

pygame.init()
FPS = 60
BLUE = (0, 0, 255)
LIGHTGRAY = (211,211,211)

screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Tic Tac Toe')
clock = pygame.time.Clock()
header_surf = pygame.Surface((300, 100))
main_surf = pygame.Surface((300, 300))
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
    

