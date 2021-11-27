import pygame
import os
from config import *


COME_SOM = 'come_som'
NICE_MUSIC = 'nice_music'
HEAD = 'HEAD'
def load_assets():
    assets = {}
    pygame.mixer.music.load('assets/sons/musica_do_jogo.mp3')
    assets[COME_SOM] = pygame.mixer.Sound('assets/sons/cobra_comendo.wav')
