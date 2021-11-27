import pygame
from config import *
import sprites
from os import *
from typing_extensions import runtime
from pygame.constants import QUIT
from pygame.math import *


# Construindo a comida
class Comida():
    def __init__(self):
        self.x_comida = randint(0, 600)
        self.y_comida = randint(0, 600)
        self.posicao_comida = Vector2(self.x_comida, self.y_comida)
    
    
    def desenhar_fruta(self):
        fruta = pygame.Rect(self.posicao_comida.x, self.posicao_comida.y, LARGURA, ALTURA)