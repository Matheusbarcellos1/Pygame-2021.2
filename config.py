from random import randint
import pygame


# Comprimentos da tela do jogo + tela do jogo (valores não fixos, sujeitos a alterações)
LARGURA = 700
ALTURA = 700
MEDIDAS_TELA = (LARGURA, ALTURA)
JANELA = pygame.display.set_mode(MEDIDAS_TELA)


# Coordenadas iniciais da cobra (valores não fixos, sujeitos a alterações/baseados nas medidas da tela do jogo)
X_COBRA = (LARGURA / 2) - (10 / 2)
Y_COBRA = (ALTURA / 2) - (10 / 2)


# Definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
AMARELO = (244, 233, 51)

INIT = 0
GAME = 1
QUIT = 2

# Pontos
PONTOS = 0
window = JANELA

# Coordenadas comida (RETIRAR)
X_COMIDA = randint(0, 600)
Y_COMIDA = randint(0, 600)


# Coordenadas de velocidade de movimento
velocidade = 5
vel_x = velocidade
vel_y = 0


# Pontos
pontos = 0


lista_cobra = [] # Para aumento de tamanho
COMPRIMENTO_INICIAL = 1
state = True # Mantém laço do while enquanto verdadeiro
morte = False # Variável para quando a cobra de morde


# Nome do jogo
TITULO_JOGO = 'PAC-SNAKE'

# Frames por segundo (FPS)
FPS = 60


# Imagens
SPRITESHEET = 'spritesheet.png'
PACSNAKE_LOGO = 'pacsnake_logo.png'


# Fonte
FONTE = 'arial'


# Áudios
SOM_INICIO = 'arquivo.mp3'
TECLA_INICIO = 'munch_1.wav'
SOM_JOGO = 'musica_do_jogo.mp3'
SOM_COMER = ''
