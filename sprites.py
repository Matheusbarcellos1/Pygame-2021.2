import random
import pygame
from config import *
from pygame.math import Vector2 
class SNAKE():
    def __init__(self):
        # Definindo coordenadas do corpo da cobra
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        
        # Carregando as imagens
        self.head_up = pygame.image.load('imagens/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('imagens/head_down.png').convert_alpha()
        self.head_right = pygame.image.load('imagens/head_right.png').convert_alpha()
        self.head_left = pygame.image.load('imagens/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load('imagens/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('imagens/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load('imagens/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load('imagens/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load('imagens/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load('imagens/body_horizontal.png').convert_alpha()

        self.body_tl = pygame.image.load('imagens/body_tl.png').convert_alpha()
        self.body_tr = pygame.image.load('imagens/body_tr.png').convert_alpha()
        self.body_br = pygame.image.load('imagens/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load('imagens/body_bl.png').convert_alpha()

        #Carregando Sonos do jogo
        self.crunch_sound = pygame.mixer.Sound('musica_sons/cobra_comendo.wav')
        self.game_music_sound = pygame.mixer.Sound('musica_sons/musica_do_jogo.mp3')
        
    def update_head_graphics(self):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): 
            self.head = self.head_left
        elif head_relation == Vector2(-1,0): 
            self.head = self.head_right
        elif head_relation == Vector2(0,1): 
            self.head = self.head_up
        elif head_relation == Vector2(0,-1): 
            self.head = self.head_down

    def update_tail_graphics(self):
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): 
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): 
            self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): 
            self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): 
            self.tail = self.tail_down    

    

    def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
    
    def add_block(self):
        self.new_block = True

    def play_crunch_sound(self):
        self.crunch_sound.play()

    def play_game_music_sound(self):
        self.game_music_sound.play()

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        

class FRUIT():
    def __init__(self):
        self.x = random.randint(0, cell_number - 2)
        self.y = random.randint(0, cell_number - 2)
        self.pos = Vector2(self.x, self.y)
