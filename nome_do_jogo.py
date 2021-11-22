import pygame
import random


# from config import **,**,**,**,**
# from tela_do_jogo import *jogo*
# form init/end _screen import tela inicial e final

# Definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Comprimentos da tela do jogo (valores não fixos, sujeitos a alterações)
largura = 800
altura = 700
medidas = (largura, altura)


pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode(medidas) # Subistituir dps 0 pelo valor correto
pygame.display.set_caption('Nome do Jogo') # Adicionar nome do jogo depois

# Coordenadas iniciais da cobra (valores não fixos, sujeitos a alterações/baseados nas medidas da tela do jogo)
x = 400
y = 350

# Velocidade inicial de movimento da cobra
vel_cobra = 10

state = True
while state != False:
    pygame.time.delay(50)

    if state == True:
        state = 1
    elif state == 1:
        state = [0,'x']
    else:
        state = False

    for event in pygame.event.get():        #fecha a janela do jogo  
        if event.type == pygame.QUIT:
            state = False

    # Comandos de movimentos da cobra
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= vel_cobra
    if comandos[pygame.K_DOWN]:
        y += vel_cobra
    if comandos[pygame.K_RIGHT]:
        x += vel_cobra
    if comandos[pygame.K_LEFT]:
        x -= vel_cobra

    # Atualiza a tela para apagar os passos pecorridos pela cobra
    window.fill(PRETO) # A cor deve ser a mesma do fundo da tela!

    pygame.draw.circle(window, VERMELHO, (x, y), 10)
    pygame.display.update()

pygame.quit()