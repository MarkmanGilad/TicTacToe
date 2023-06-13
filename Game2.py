# events

import pygame
from Graphics import *
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')

def main ():
    run = True

    while (run):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False

        pygame.display.update()
    

if __name__ == '__main__':
    main()
