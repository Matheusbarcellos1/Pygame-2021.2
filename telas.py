from os import X_OK
import pygame, sys, random
from pygame.math import Vector2
from assets import load_assets
from config import *
from classes import *

def tela_inicio(screen,assets):
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 48)
    font1= pygame.font.SysFont(None, 80)
    Titulo = font1.render('SnA-PaC GaMe', True, (140, 50,50))
    start = font.render('Press "enter" to start', True, (0, 0, 0))
    keys_down = {}
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = DONE
                running = False

            if event.type == pygame.KEYDOWN:
                
                keys_down[event.key] = True
                if event.key == pygame.K_RETURN:
                        state = PLAYING
                        running = False

        screen.fill((255, 255, 255))
        screen.blit(assets["tela_inicio"], (0, 0))
        screen.blit(Titulo,(160,100))
        screen.blit(start,(cell_number * cell_size / 3 - 50, cell_number * cell_size / 2 + 300))
        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

def tela_jogo(tela,jogo,assets):
    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    clock = pygame.time.Clock()
    DONE = 0
    JOGANDO = 1
    MORTO = 3
    state = JOGANDO

    keys_down = {}
    score = 0
    game = RUNNING
    while state != MORTO:
        
        for event in pygame.event.get():          
            if event.type == pygame.QUIT:           # Fecha a janela do jogo quando aperta no 'X' da tela
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE and game != PAUSED:
                jogo.update()
                print('EU Esotu')
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    if jogo.snake.direction.y != 1:
                        jogo.snake.direction = Vector2(0, -1)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    if jogo.snake.direction.y != -1:
                        jogo.snake.direction = Vector2(0, 1)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    if jogo.snake.direction.x != -1:
                        jogo.snake.direction = Vector2(1, 0)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    if jogo.snake.direction.x != 1:
                        jogo.snake.direction = Vector2(-1, 0)
                if event.key == pygame.K_p:  # Em caso de apertar a tecla "p", pausa o jogo
                    if game != PAUSED:
                        game = PAUSED
                        pygame.mixer.pause()
                    else:
                        pygame.mixer.unpause()
                        game = RUNNING
        if game == PAUSED:
            pygame.display.flip()
            continue
                
        pygame.display.update()
        tela.fill((175, 215, 70))
        jogo.draw_elements(tela)
        pygame.display.update()
        jogo.update(assets)
        clock.tick(FPS)

        return state

def tela_game_over():
    return None
    