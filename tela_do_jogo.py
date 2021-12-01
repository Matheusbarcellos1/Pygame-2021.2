import pygame
from config import *
from assets import *
from sprites import *
from tentativa_final import FRUIT

def tela_do_jogo(tela):

    clock = pygame.time.Clock()
    all_bodies = pygame.sprite.Group()
    all_fruits = pygame.sprite.Group()

    groups = {}
    groups['frutas'] = all_fruits
    groups['corpos'] = all_bodies

    cobra = SNAKE()
    all_bodies.add(cobra)

    fruta = FRUIT()
    all_fruits.add(fruta)

    DONE = 0
    PLAYING = 1
    DEAD = 3
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0

    pygame.mixer.music.play(loops = -1)
    while state!= DONE:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                state = DONE
            
            if state == PLAYING:

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if cobra.direction.y != 1:
                            cobra.direction = Vector2(0, -1)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if cobra.direction.y != -1:
                            cobra.direction = Vector2(0, 1)
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if cobra.direction.x != -1:
                            cobra.direction = Vector2(1, 0)
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if cobra.direction.x != 1:
                            cobra.direction = Vector2(-1, 0)
        
        #all_sprites.update()
        cobra.move_snake()

        if state == PLAYING:
            
            #checa se a cobra comeu uma fruta ou se a fruta apareceu no meio do corpo da cobra
            if fruta.pos == cobra.body[0]:
                fruta.kill()
                fruta = FRUIT()
                all_fruits.add(fruta)
                cobra.add_block()
                #play crunch sound

            for block in cobra.body[1:]:
                if block == fruta.pos:
                    fruta.kill()
                    fruta = FRUIT()
            
            
            #checa colisão da cobra com seu próprio corpo
            if not 0 <= cobra.body[0].x < cell_number or not 0 <= cobra.body[0].y < cell_number:
                state = DEAD
                cobra.kill()

            for block in cobra.body[1:]:
                if block == cobra.body[0]:
                    state = DEAD
                    cobra.kill()
            
        cobra.draw_snake(tela)
        fruta.draw_fruit(tela)


    #criando os corpos do jogo
    return state