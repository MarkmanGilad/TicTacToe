# events

import pygame
pygame.init()

screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('pygame')

def main ():
    run = True

    while (run):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False
               # break

        pygame.display.update()
    
    pygame.quit()

if __name__ == '__main__':
    main()
