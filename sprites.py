import random
import pygame
from config import *
from assets import *

class Corpo(pygame.sprite.Sprite):
    def __init__(self,groups,assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets[HEAD]
        