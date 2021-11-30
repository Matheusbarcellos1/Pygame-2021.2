import pygame, sys, random
from pygame.math import Vector2
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.4)
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
        
        

    def draw_snake(self):
        self.update_head_graphics()
        self.update_tail_graphics()

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
        self.randomize()

    def draw_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)
        screen.blit(apple, fruit_rect)
    
    def randomize(self):
        self.x = random.randint(0, cell_number - 2)
        self.y = random.randint(0, cell_number - 2)
        self.pos = Vector2(self.x, self.y)

class MAIN():
    def __init__(self):
        self.snake = SNAKE()
        self.fruit = FRUIT()
        self.snake.play_game_music_sound()
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()

    def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.add_block()
            self.snake.play_crunch_sound()

        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        self.snake.reset()
    
    def draw_grass(self):
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

    def draw_score(self):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text, True, (56, 74, 12))
        score_x = int(cell_size * cell_number - 60)
        score_y = int(cell_size * cell_number - 60)
        score_rect = score_surface.get_rect(center = (score_x, score_y))
        apple_rect = apple.get_rect(midright = (score_rect.left, score_rect.centery))
        bg_rect = pygame.Rect(apple_rect.left, apple_rect.top, apple_rect.width + score_rect.width + 10, apple_rect.height)

        pygame.draw.rect(screen, (167, 209, 61), bg_rect)
        screen.blit(score_surface, score_rect)
        screen.blit(apple, apple_rect)
        pygame.draw.rect(screen, (56, 74, 12), bg_rect, 2)

cell_size = 20
cell_number = 35
tela_inicio = window = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #cria a tela do jogo
window = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #cria a tela do jogo
#Printando a tela
font = pygame.font.SysFont(None, 48)
font1= pygame.font.SysFont(None, 80)
Titulo = font1.render('Jogo da cobra', True, (140, 50,50))
start = font.render('Press "enter" to start', True, (0, 0, 0))
game_over = font1.render('Game Over', True, (0, 0, 0))
novamente = font.render('Quer jogar novamente? Pressione Enter', True, (0, 0, 0))

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
apple = pygame.image.load('imagens/food.png').convert_alpha()
game_font = pygame.font.Font(None, 25)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()
#assets
def load_assets():
    assets= {}
    assets['tela de inicio'] = pygame.image.load('imagens/tela_inicio.jpg').convert() 
    assets['tela de inicio'] = pygame.transform.scale(assets["tela de inicio"], (cell_number * cell_size, cell_number * cell_size))
    assets['final'] = pygame.image.load('imagens/cobra.jpg').convert_alpha() 
    assets['final'] = pygame.transform.scale(assets["final"], (cell_number * cell_size, cell_number * cell_size)) 
    return assets

keys_down = {}
#Estado do jogo
DONE = 0 #o jogo terminou
PLAYING = 1 #o jogador está jogando
TELA = 2
FINAL = 3
state = TELA
assets = load_assets()
list_lives = []
vidas = 0
if len(list_lives) == 1:
    vidas = 0
if len(list_lives) == 2:
    state = FINAL
#Definindo os frames por segundo para ajustar a velocidade da bola
clock = pygame.time.Clock()
#Trata eventos
while state == TELA:
        window.fill((255, 255, 255))
        window.blit(assets["tela de inicio"], (0, 0))
        window.blit(Titulo,(50,150))
        window.blit(start,(50,250))
        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    state = DONE
            if state == TELA:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_RETURN:
                            state = PLAYING
                            
while state == FINAL:
        window.fill((255, 255, 255))
        window.blit(assets["final"], (0, 0))
        window.blit(game_over,(75,150))
        pygame.display.update() 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = DONE
            if state == FINAL:
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_RETURN:
                        state = PLAYING
                    else:
                        state = DONE
        window.fill((255, 255, 255))
        window.blit(assets["tela de inicio"], (0, 0))
    
while True:
    for event in pygame.event.get():          
        if event.type == pygame.QUIT:           # Fecha a janela do jogo quando aperta no 'X' da tela
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                if main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
            
    pygame.display.update()
    screen.fill((175, 215, 70))
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(200)