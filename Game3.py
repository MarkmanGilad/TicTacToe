# clock & Frame Per Second

import pygame
pygame.init()

screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Pygame')
clock = pygame.time.Clock()


def main ():
    run = True

    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False

        # The code


        pygame.display.update()
        clock.tick(60)  # FPS
    

if __name__ == '__main__':
    main()
