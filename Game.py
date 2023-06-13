import pygame
from Graphics import *
from TicTacToe import TicTacToe
from Human_Agent import Human_Agent

pygame.init()

clock = pygame.time.Clock()
graphics = Graphics()
env = TicTacToe(State())
player1 = Human_Agent(1, env, graphics)
player2 = Human_Agent(-1, env,graphics)
player = player1

def main ():
    run = True
    
    while (run):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False
        action = player(events)
        if action:
            env.move(action)
            switch_players(player)
            if env.state.end_of_game != 0:
                run = False

        graphics(env.state)
        clock.tick(FPS)
    
    pygame.time.wait(2000)
    

def switch_players(player):
    if player == player1:
        player = player2
    else:
        player = player1

if __name__ == '__main__':
    main()
