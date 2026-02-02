# User Interface

import pygame
pygame.init()

screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Reversi')
clock = pygame.time.Clock()
header_surf = pygame.Surface((300, 100))
main_surf = pygame.Surface((300, 300))
header_surf.fill('BLUE')
main_surf.fill('LIGHTGRAY')


pygame.draw.line(surface=main_surf, color='BLACK', start_pos=(10,10), end_pos=(100,100), width=5)
pygame.draw.circle(surface=main_surf, color='GREEN' , center= (50,50), radius=20, width=2)
pygame.draw.circle(surface=header_surf, color='RED', center= (150,50), radius=30, width=0)
screen.blit(header_surf, (0,0))
screen.blit(main_surf, (0,100))

x_img = pygame.image.load("img/x_img.png")
x_img = pygame.transform.scale(x_img, (40, 40))


def main ():
    run = True
    
    while (run):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                #x,y = pygame.mouse.get_pos()
                x, y = event.pos
                pos = x - 20, y -100 - 20
                main_surf.blit(x_img,pos)
                print(events)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    header_surf.fill('GREEN')
                if event.key == pygame.K_RIGHT:
                    header_surf.fill('CADETBLUE1')
                    

        screen.blit(header_surf, (0,0))
        screen.blit(main_surf, (0,100))
        pygame.display.update()
        clock.tick(60)
    

if __name__ == '__main__':
    main()
