# pygame main loop
import pygame

pygame.init()

WIDTH, HEIGHT = 300, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')

def main ():
    run = True

    while (run):
        pygame.display.update()


if __name__ == '__main__':
    main()


