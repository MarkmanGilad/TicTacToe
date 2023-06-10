import pygame
from Graphics import *
pygame.init()


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Reversi')

def main ():
    run = True

    while (run):
        pygame.display.update()


if __name__ == '__main__':
    main()
