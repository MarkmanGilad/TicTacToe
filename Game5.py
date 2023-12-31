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

pygame.draw.line(surface=main_surf, color=BLACK, start_pos=(10,10), end_pos=(100,100), width=5)
pygame.draw.circle(surface=main_surf, color=GREEN, center= (150,150), radius=40, width=5)
pygame.draw.circle(surface=header_surf, color=RED, center= (150,50), radius=30, width=0)

screen.blit(header_surf, (0,0))
screen.blit(main_surf, (0,100))


def main ():
    run = True
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            

        pygame.display.update()
        clock.tick(FPS)
    

if __name__ == '__main__':
    main()
