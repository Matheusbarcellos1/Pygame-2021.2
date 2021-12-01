import pygame
from config import *
from tela_inicial import init_tela, game_over
from tela_do_jogo import tela_do_jogo

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #cria a tela do jogo
pygame.display.set_caption('Pacobrinha')

state = INIT

while state != QUIT:
    
    if state == INIT:
        state = init_tela(tela)
    
    elif state == GAME:
        state = tela_do_jogo(tela)
    
    elif state == DEAD:
        state = game_over(tela)
    else:
        state = QUIT

pygame.quit()