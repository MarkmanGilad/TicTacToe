import pygame

pygame.init()



def main ():

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Images')
    clock = pygame.time.Clock()

    screen.fill('LIGHTGRAY')

    img = pygame.image.load("img/space_ship.png")
    img = pygame.transform.scale(img, (50, 50))

    x, y = 0, 0
    vx, vy = 2, 0
    
    run = True
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False

        screen.fill('LIGHTGRAY') 
        screen.blit(img, (x, y))
        # תרגיל א
        x = x + 1
        y = y + 2
        # תרגיל ב
        
        pygame.display.update()
        clock.tick(60)
    

if __name__ == '__main__':
    main()