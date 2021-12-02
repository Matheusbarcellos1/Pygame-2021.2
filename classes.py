from os import X_OK
import pygame, sys, random
from pygame.math import Vector2
from assets import load_assets
from config import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.4)

#Carrega os sprites e sons de um arquivo separado
tela = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #cria a tela do jogo
pygame.display.set_caption('Pacobrinha')

crunch = pygame.mixer.Sound('musica_sons/cobra_comendo.wav')
music = pygame.mixer.Sound('musica_sons/musica_do_jogo.mp3')

class SNAKE():
    def __init__(self,assets):
        # Definindo coordenadas do corpo da cobra
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.new_block = False
        
        # Carregando as imagens de assets
        self.head_up = assets['head_up']
        self.head_down = assets['head_down']
        self.head_right = assets['head_right']
        self.head_left = assets['head_left']

        self.tail_up = assets['tail_up']
        self.tail_down = assets['tail_down']
        self.tail_right = assets['tail_right']
        self.tail_left = assets['tail_left']

        self.body_vertical = assets['body_vertical']
        self.body_horizontal = assets['body_horizontal']

        self.body_tl = assets['body_tl']
        self.body_tr = assets['body_tr']
        self.body_br = assets['body_br']
        self.body_bl = assets['body_bl']


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

    def reset(self):
        self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
        self.direction = Vector2(0,0)
        

class FRUIT():
    def __init__(self,assets):
        self.x = random.randint(0, cell_number - 2)
        self.y = random.randint(0, cell_number - 2)
        self.pos = Vector2(self.x, self.y)
        self.apple = assets['apple']

    

class MAIN2():
    def __init__(self,screen,assets):
        self.snake = SNAKE(assets)
        self.fruit = FRUIT(assets)
        self.rock1 = Obstacle(assets)
        self.rock2 = Obstacle(assets)
        self.rock3 = Obstacle(assets)
        music.play()
        self.game_font = pygame.font.Font(None, 25)

    def update(self,assets):
        self.snake.move_snake()
        self.check_collision(assets)
        self.check_fail()

    def draw_elements(self,tela):
        self.draw_grass(tela)
        self.draw_fruit(tela)
        self.draw_snake(tela)
        self.draw_score(tela)
        self.draw_rock(tela)

    def draw_fruit(self,screen):
        fruit_rect = pygame.Rect(int(self.fruit.pos.x * cell_size), int(self.fruit.pos.y * cell_size), cell_size, cell_size)
        screen.blit(self.fruit.apple, fruit_rect)
    
    def draw_rock(self,screen):
        rock_rect1 = pygame.Rect(int(self.rock1.pos.x * cell_size), int(self.rock1.pos.y * cell_size), 2*cell_size, 2*cell_size)
        rock_rect2 = pygame.Rect(int(self.rock2.pos.x * cell_size), int(self.rock2.pos.y * cell_size), 2*cell_size, 2*cell_size)
        rock_rect3 = pygame.Rect(int(self.rock3.pos.x * cell_size), int(self.rock3.pos.y * cell_size), 2*cell_size, 2*cell_size)
        screen.blit(self.rock2.image, rock_rect1)
        screen.blit(self.rock2.image, rock_rect2)
        screen.blit(self.rock2.image, rock_rect3)

    def draw_snake(self,screen):
        self.snake.update_head_graphics()
        self.snake.update_tail_graphics()

        for index, block in enumerate(self.snake.body):
            x_pos = int(block.x * cell_size)
            y_pos = int(block.y * cell_size) 
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                screen.blit(self.snake.head, block_rect)    
            elif index == len(self.snake.body) - 1:
                screen.blit(self.snake.tail, block_rect)
            else:
                previous_block = self.snake.body[index + 1] - block
                next_block = self.snake.body[index - 1] - block
                if previous_block.x == next_block.x:
                    screen.blit(self.snake.body_vertical, block_rect)
                if previous_block.y == next_block.y:
                    screen.blit(self.snake.body_horizontal, block_rect)
                else:
                    if previous_block.x == -1 and next_block.y == - 1 or previous_block.y == -1 and next_block.x == -1: 
                        screen.blit(self.snake.body_tl, block_rect)
                    elif previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1: 
                        screen.blit(self.snake.body_bl, block_rect)
                    elif previous_block.x == 1 and next_block.y == - 1 or previous_block.y == -1 and next_block.x == 1: 
                        screen.blit(self.snake.body_tr, block_rect)
                    elif previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1: 
                        screen.blit(self.snake.body_br, block_rect)
    
    
    def check_collision(self,assets):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit = FRUIT(assets)
            self.snake.add_block()
            crunch.play()
        if self.fruit.pos == self.rock1.pos or self.fruit.pos == self.rock1.pos + Vector2(1,0) or self.fruit.pos == self.rock1.pos + Vector2(0,1) or self.fruit.pos == self.rock1.pos + Vector2(1,1) or self.fruit.pos == self.rock2.pos or self.fruit.pos == self.rock2.pos + Vector2(1,0) or self.fruit.pos == self.rock2.pos + Vector2(0,1) or self.fruit.pos == self.rock2.pos + Vector2(1,1) or self.fruit.pos == self.rock3.pos or self.fruit.pos == self.rock3.pos + Vector2(1,0) or self.fruit.pos == self.rock3.pos + Vector2(0,1) or self.fruit.pos == self.rock3.pos + Vector2(1,1):
            self.fruit = FRUIT(assets)
        for block in self.snake.body[1:]: # Colisão entre a cobra e a comida
            if block == self.fruit.pos:
                self.fruit = FRUIT(assets)
            if block == self.rock1.pos or block == self.rock1.pos + Vector2(1,0) or block == self.rock1.pos + Vector2(0,1) or block == self.rock1.pos + Vector2(1,1):
                self.snake.reset()
                self.rock1 = Obstacle(assets)
            if block == self.rock2.pos or block == self.rock2.pos + Vector2(1,0) or block == self.rock2.pos + Vector2(0,1) or block == self.rock2.pos + Vector2(1,1):
                self.snake.reset()
                self.rock2 = Obstacle(assets)
            if block == self.rock3.pos or block == self.rock3.pos + Vector2(1,0) or block == self.rock3.pos + Vector2(0,1) or block == self.rock3.pos + Vector2(1,1):
                self.snake.reset()
                self.rock3 = Obstacle(assets)

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.snake.reset()

        for block in self.snake.body[1:]: # Colisão quando a cobra morde o corpo ou a cauda
            if block == self.snake.body[0]:
                self.snake.reset()
 
    # Desenha na tela do mato como plano de fundo
    def draw_grass(self,screen):
        grass_color = (167, 209, 61)
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect) 
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect) 

    # Desenha na tela os pontos do jogador
    def draw_score(self,screen):
        score_text = str(len(self.snake.body) - 3)
        score_surface = self.game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 60)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = self.fruit.apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 10, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(self.fruit.apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)
    
class Obstacle():
    def __init__(self,assets):
        self.x = random.randint(3,cell_number-3)
        self.y = random.randint(3,cell_number-3)
        self.pos = Vector2(self.x, self.y)
        
        self.image = assets['rock']
        
    


