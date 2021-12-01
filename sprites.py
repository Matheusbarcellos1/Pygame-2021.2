import random
import pygame
from config import *
from assets import *
from pygame.math import Vector2

class SNAKE(pygame.sprite.Group):
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

        #Carregando Sons do jogo
        self.crunch_sound = pygame.mixer.Sound('musica_sons/cobra_comendo.wav')
        self.game_music_sound = pygame.mixer.Sound('musica_sons/musica_do_jogo.mp3')       

    def draw_snake(self,screen):
        head_relation = self.body[1] - self.body[0]
        if head_relation == Vector2(1,0): 
            self.head = self.head_left
        elif head_relation == Vector2(-1,0): 
            self.head = self.head_right
        elif head_relation == Vector2(0,1): 
            self.head = self.head_up
        elif head_relation == Vector2(0,-1): 
            self.head = self.head_down
        
        tail_relation = self.body[-2] - self.body[-1]
        if tail_relation == Vector2(1,0): 
            self.tail = self.tail_left
        elif tail_relation == Vector2(-1,0): 
            self.tail = self.tail_right
        elif tail_relation == Vector2(0,1): 
            self.tail = self.tail_up
        elif tail_relation == Vector2(0,-1): 
            self.tail = self.tail_down  

        for index, block in enumerate(self.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size) 
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.head, block_rect)    
            elif index == len(self.body) - 1:
                screen.blit(self.tail, block_rect)
            else:
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.body_vertical, block_rect)
                if previous_block.y == next_block.y:
                    screen.blit(self.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == - 1 or previous_block.y == -1 and next_block.x == -1: 
                        screen.blit(self.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: 
                        screen.blit(self.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == - 1 or previous_block.y == -1 and next_block.x == 1: 
                        screen.blit(self.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1: 
                        screen.blit(self.body_br, block_rect)

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


class FRUIT():
    def __init__(self):
        self.x = random.randint(0, cell_number - 2)
        self.y = random.randint(0, cell_number - 2)
        self.pos = Vector2(self.x, self.y)
        

    def draw_fruit(self,screen,apple):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
    
        