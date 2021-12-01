import pygame
import random
from config import *
from tela_inicial import init_tela
from tela_do_jogo import tela_do_jogo

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode(MEDIDAS_TELA)
pygame.display.set_caption('Pacobrinha')

state = INIT

while state != QUIT:
    
    if state == INIT:
        state = init_tela(tela)
    
    elif state == GAME:
        state = tela_do_jogo(tela)
    
    else:
        state = QUIT

pygame.quit()