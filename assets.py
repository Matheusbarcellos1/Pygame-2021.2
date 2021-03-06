import pygame
import os
from config import *


pygame.mixer.init()
pygame.init()
def load_assets(tela):
    assets = {}
    assets['head_up'] = pygame.image.load('imagens/head_up.png').convert_alpha()
    assets['head_down'] = pygame.image.load('imagens/head_down.png').convert_alpha()
    assets['head_right'] = pygame.image.load('imagens/head_right.png').convert_alpha()
    assets['head_left'] = pygame.image.load('imagens/head_left.png').convert_alpha()

    assets['tail_up'] = pygame.image.load('imagens/tail_up.png').convert_alpha()
    assets['tail_down'] = pygame.image.load('imagens/tail_down.png').convert_alpha()
    assets['tail_right'] = pygame.image.load('imagens/tail_right.png').convert_alpha()
    assets['tail_left'] = pygame.image.load('imagens/tail_left.png').convert_alpha()

    assets['body_vertical'] = pygame.image.load('imagens/body_vertical.png').convert_alpha()
    assets['body_horizontal'] = pygame.image.load('imagens/body_horizontal.png').convert_alpha()

    assets['body_tl'] = pygame.image.load('imagens/body_tl.png').convert_alpha()
    assets['body_tr'] = pygame.image.load('imagens/body_tr.png').convert_alpha()
    assets['body_br'] = pygame.image.load('imagens/body_br.png').convert_alpha()
    assets['body_bl'] = pygame.image.load('imagens/body_bl.png').convert_alpha()

    assets['apple'] = pygame.image.load('imagens/food.png').convert_alpha()

    assets['tela_inicio'] = pygame.image.load('imagens/tela_inicio.jpg').convert() 
    assets['tela_inicio'] = pygame.transform.scale(assets['tela_inicio'], (cell_number * cell_size, cell_number * cell_size))
    assets['final'] = pygame.image.load('imagens/cobra.jpg').convert_alpha() 
    assets['final'] = pygame.transform.scale(assets['final'], (cell_number * cell_size, cell_number * cell_size)) 
    
    assets['rock'] = pygame.image.load('imagens/rock.png').convert_alpha()
    assets['rock'] = pygame.transform.scale(assets['rock'], (2*cell_size, 2*cell_size))
    assets['head_up'] = pygame.transform.scale(assets['head_up'], (cell_size, cell_size))
    assets['head_down'] = pygame.transform.scale(assets['head_down'], (cell_size, cell_size))
    assets['head_right'] = pygame.transform.scale(assets['head_right'], (cell_size, cell_size))
    assets['head_left'] = pygame.transform.scale(assets['head_left'], (cell_size, cell_size))
    assets['tail_up'] = pygame.transform.scale(assets['tail_up'], (cell_size, cell_size))
    assets['tail_down'] = pygame.transform.scale(assets['tail_down'], (cell_size, cell_size))
    assets['tail_right'] = pygame.transform.scale(assets['tail_right'], (cell_size, cell_size))
    assets['tail_left'] = pygame.transform.scale(assets['tail_left'], (cell_size, cell_size))
    assets['body_vertical'] = pygame.transform.scale(assets['body_vertical'], (cell_size, cell_size))
    assets['body_horizontal'] = pygame.transform.scale(assets['body_horizontal'], (cell_size, cell_size))
    assets['body_tl'] = pygame.transform.scale(assets['body_tl'], (cell_size, cell_size))
    assets['body_tr'] = pygame.transform.scale(assets['body_tr'], (cell_size, cell_size))
    assets['body_br'] = pygame.transform.scale(assets['body_br'], (cell_size, cell_size))
    assets['body_bl'] = pygame.transform.scale(assets['body_bl'], (cell_size, cell_size))
    
    assets['apple'] = pygame.transform.scale(assets['apple'], (cell_size, cell_size))
    
    
    
    
    #Carregando Sonos do jogo
    assets['nham'] = pygame.mixer.Sound('musica_sons/cobra_comendo.wav')
    assets['game_sound'] = pygame.mixer.Sound('musica_sons/musica_do_jogo.mp3')
    return assets
