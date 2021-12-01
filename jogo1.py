import pygame
from config import *
from classes import *
from telas import *
from assets import load_assets


pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #cria a tela do jogo
pygame.display.set_caption('Pacobrinha')

assets = load_assets(tela)
jogo = MAIN2(tela,assets)
state = TELA


while state != DONE:
    
    if state == TELA:
        state = tela_inicio(tela,assets)
    
    elif state == PLAYING:
        state = tela_jogo(tela,jogo,assets)
    
    elif state == DEAD:
        state = tela_game_over(tela)

    else:
        state = DONE

pygame.quit()