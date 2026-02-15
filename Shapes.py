# draw shapes

import pygame
pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Shapes')
clock = pygame.time.Clock()
screen.fill('lightgray')



pygame.draw.line(surface=screen, color='BLACK', start_pos=(10,10), end_pos=(100,100), width=5)
pygame.draw.circle(surface=screen, color='GREEN', center= (150,150), radius=40, width=5)
pygame.draw.circle(surface=screen, color='RED', center= (150,50), radius=30, width=0)
pygame.draw.rect(surface=screen, color="PURPLE", rect=[50, 50, 200, 200], width=3)
pygame.draw.rect(surface=screen, color="ORANGE", rect=[300, 50, 200, 200], width=0)
pygame.draw.ellipse(surface=screen, color='BLUE', rect=[50, 300, 200, 100], width=0)
pygame.draw.polygon(surface=screen, color='YELLOW', points=[(300,300), (400,300), (350,400)], width=0)

def main ():
    run = True
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            

        pygame.display.update()
        clock.tick(60)
    

if __name__ == '__main__':
    main()
