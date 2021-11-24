import pygame
from random import randint
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP, KEYDOWN, QUIT, K_a, K_d, K_r, K_s, K_w # O que é isso??????
from config import *
from sys import exit


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


lista_cobra = [] # Para aumento de tamanho
comprimento_inicial = 1
state = True # Mantém laço do while enquanto verdadeiro
morte = False # Variável para quando a cobra de morde

# DEFININDO A FUNÇÃO DE TAMANHO DA OBRA (OBS: RETIRAR DAQUI DEPOIS)
def cresce_cobra(lista_cobra):
    for posicao in lista_cobra:
        # Lembrando que lista_cobra é uma lista dentro de lista: [[x, y]]
        pygame.draw.rect(window, VERDE, (posicao[0], posicao[1], 10, 10))

# DEFININDO A FUNÇÃO DE REINICIAR O JOGO QUANDO A COBRA SE MORDE (OBS: RETIRAR DAQUI DEPOIS)
def reinicia_jogo():

    # Redefinindo as variáveis locais
    global pontos, comprimento_inicial, x_cobra, y_cobra, x_comida, y_comida, lista_cobra, lista_cabeca, morte
    pontos = 0
    comprimento_inicial = 1
    x_cobra = (largura / 2) - (10 / 2)
    y_cobra = (altura / 2) - (10 / 2)
    lista_cabeca = []
    lista_cobra = []
    x_comida = randint(0, 600) 
    y_comida = randint(0, 600)
    morte = False

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
                if vel_x == velocidade:
                    pass
                else:
                    vel_x = - (velocidade + 3)
                    vel_y = 0
            if event.key == K_RIGHT or event.key == K_d:
                if vel_x == - velocidade:
                    pass
                else:
                    vel_x = velocidade + 3
                    vel_y = 0
            if event.key == K_UP or event.key == K_w:
                if vel_y == velocidade:
                    pass
                else:
                    vel_x = 0
                    vel_y = - (velocidade + 3)
            if event.key == K_DOWN or event.key == K_s:
                if vel_y == - velocidade:
                    pass
                else:
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
        comprimento_inicial += 30


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

    # Faz com que o tamanho da cobra só aumente quando ela coma uma comida
    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    cresce_cobra(lista_cobra)

    # Condição de morte da cobra
    if lista_cobra.count(lista_cabeca) > 1:
        # Mensagem gerada ao jogador morrer
        fonte2 = pygame.font.Font(None, 30)
        mensagem = ("GAME OVER! PRESSIONE 'R' PARA JOGAR NOVAMENTE!")
        texto_formatado = fonte2.render(mensagem, True, VERMELHO)
        ret_texto = texto_formatado.get_rect()

        morte = True
        while morte:
            window.fill(PRETO)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit() # mesmo que: break
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reinicia_jogo()
            ret_texto.center = (largura / 2, altura / 2)
            window.blit(texto_formatado, ret_texto)
            pygame.display.update() 

    pygame.display.update()
pygame.quit()