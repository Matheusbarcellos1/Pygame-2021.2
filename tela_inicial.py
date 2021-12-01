import pygame, sys, random
from config import *
from sprites import *



def init_tela(tela):
    clock  = pygame.time.Clock()

    background = pygame.image.load('imagens/tela_inicio.jpg').convert()
    background_rect = background.get_rect()

    running = True

    while running:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                state = GAME
                running = False
        
        tela.fill(PRETO)
        tela.blit(background,background_rect)
    
        pygame.display.flip()

    return state

def game_over(tela):
    clock  = pygame.tick.Clock()

    game_over = pygame.image.load('imagens/cobra.jpg').convert_alpha()
    game_over_rect = game_over.get_rect()

    running = True

    keys_down = {}
    while running:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                state = QUIT
                running = False
            
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_SPACE:
                    state = GAME
                
                    running = False
        
        tela.fill(PRETO)
        tela.blit(game_over,game_over_rect)
    
        pygame.display.flip()

    return state
            