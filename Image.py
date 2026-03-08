import pygame

pygame.init()



def main ():


    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Images')
    clock = pygame.time.Clock()

    screen.fill('LIGHTGRAY')
    img = pygame.image.load("img/space_ship.png")
    img = pygame.transform.scale(img, (50, 50))

    x, y = 50, 50
    screen.blit(img, (x, y))

    run = True
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            
        x += 1

        screen.blit(img, (x, y))

        pygame.display.update()
        clock.tick(60)
    

if __name__ == '__main__':
    main()