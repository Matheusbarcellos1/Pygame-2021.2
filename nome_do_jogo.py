import pygame
from random import randint

from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, K_a, K_d, K_s, K_w
from config import *


# from config import **,**,**,**,**
# from tela_do_jogo import *jogo*
# form init/end _screen import tela inicial e final


pygame.init()
pygame.mixer.init()


# Som do jogo
pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('musica_do_jogo.mp3')
pygame.mixer.music.play(-1)

# Som da cobra comendo a comimda
barulho_comendo = pygame.mixer.Sound('cobra_comendo.wav')

window = pygame.display.set_mode(medidas_tela) # Substituir dps pelo valor correto
pygame.display.set_caption('Nome do Jogo') # Adicionar nome do jogo depois
tempo = pygame.time.Clock()                 # Tempo de passada de frames no jogo!

# Coordenadas comida
x_comida = randint(0, 600)
y_comida = randint(0, 600)

# Coordenadas de velocidade de movimento
velocidade = 5
vel_x = velocidade
vel_y = 0

# Pontos
pontos = 0

# DEFININDO A FUNÇÃO DE TAMANHO DA OBRA (OBS: RETIRAR DAQUI DEPOIS)
def cresce_cobra(lista_cobra):
    for posicao in lista_cobra:
        # Lembrando que lista_cobra é uma lista dentro de lista: [[x, y]]
        pygame.draw.rect(window, VERDE, (posicao[0], posicao[1], 10, 10))
    

lista_cobra = [] # Para aumento de tamanho
comprimento_inicial = 1
state = True
while state != False:
    if state == True:
        state = 1
    elif state == 1:
        state = [0,'x']
    else:
        state = False


    tempo.tick(50)    
    for event in pygame.event.get():          
        if event.type == pygame.QUIT:           # Fecha a janela do jogo quando aperta no 'X' da tela
            state = False

        # Comandos de movimentos da cobra com teclas
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                vel_x = - (velocidade + 3)
                vel_y = 0
            if event.key == K_RIGHT or event.key == K_d:
                vel_x = velocidade + 3
                vel_y = 0
            if event.key == K_UP or event.key == K_w:
                vel_x = 0
                vel_y = - (velocidade + 3)
            if event.key == K_DOWN or event.key == K_s:
                vel_x = 0
                vel_y = velocidade + 3
    
    x_cobra += vel_x
    y_cobra += vel_y

    # Atualiza a tela para apagar os passos pecorridos pela cobra
    window.fill(PRETO) # A cor deve ser a mesma do fundo da tela!

    # Marcador de pontos
    fonte = pygame.font.Font(None, 48)
    marcador_pontos = fonte.render(f'Pontos: {pontos}', True, VERMELHO) # Pontos com fonte
    window.blit(marcador_pontos, [0, 0])

    
    # Cobra e comida
    cobra = pygame.draw.rect(window, VERDE, (x_cobra, y_cobra, 10, 10))
    comida = pygame.draw.rect(window, VERMELHO, (x_comida, y_comida, 20, 20)) 

    # Cobra comendo a comida
    if cobra.colliderect(comida):
        x_comida = randint(0, 600) 
        y_comida = randint(0, 600)
        pontos += 1
        barulho_comendo.play()
        comprimento_inicial += 1


    # Fazendo a cobra retornar ao lado oposto quando chegar aos extremos
    if y_cobra >=  altura:
        y_cobra = 0
    elif y_cobra <= 0:
        y_cobra = altura        
    if x_cobra >= largura:
        x_cobra = 0
    elif x_cobra <= 0:
        x_cobra = largura

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    cresce_cobra(lista_cobra)


    pygame.display.update()

pygame.quit()