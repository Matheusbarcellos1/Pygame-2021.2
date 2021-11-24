from typing_extensions import runtime
import pygame
from pygame.constants import QUIT
from config import *


def init_tela(tela):
    #variável de ajuste da velocidade da atualização
    clock = pygame.time.Clock()

    #carrega a tela de fundo
    tela_inicial = pygame.image.load('assets/img/"TELA DE FUNDO".png').convert()
    tela_inicial_rect = tela_inicial.get_rect()

    running = True
    while running:

        # Ajusta a velocidade de atualização
        clock.tick(FPS)

        for event in pygame.event.get():
            #Verifica se o jogo foi fechado ou iniciado
            if event.type == pygame.QUIT():
                state = QUIT
                running = False
            
            if event.type == pygame.KEYUP:
                state = GAME
                running = False
        
        #SEmpre redesenha o fundo
        tela.fill(PRETO)
        tela.blit(tela_inicial,tela_inicial_rect)
        
        #Depois inverte o display (Pq?)
        pygame.display.flip()
    
    return state