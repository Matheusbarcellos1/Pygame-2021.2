import pygame
from random import randint
from config import PRETO, VERMELHO, VERDE, BRANCO, AZUL
from config import medidas_tela, x, y, vel_cobra, largura, altura


# from config import **,**,**,**,**
# from tela_do_jogo import *jogo*
# form init/end _screen import tela inicial e final


pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode(medidas_tela) # Substituir dps pelo valor correto
pygame.display.set_caption('Nome do Jogo') # Adicionar nome do jogo depois
tempo = pygame.time.Clock()                 # Tempo de passada de frames no jogo!

# Coordenadas comida
x_comida = randint(0, 600)
y_comida = randint(0, 600) 

state = True
while state != False:
    tempo.tick(50)

    if state == True:
        state = 1
    elif state == 1:
        state = [0,'x']
    else:
        state = False

    for event in pygame.event.get():        #fecha a janela do jogo  
        if event.type == pygame.QUIT:
            state = False


    # Comandos de movimentos da cobra com teclas
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP] or comandos[pygame.K_w]:
        y -= vel_cobra
    if comandos[pygame.K_DOWN] or comandos[pygame.K_s]:
        y += vel_cobra
    if comandos[pygame.K_RIGHT] or comandos[pygame.K_d]:
        x += vel_cobra
    if comandos[pygame.K_LEFT] or comandos[pygame.K_a]:
        x -= vel_cobra

    # Atualiza a tela para apagar os passos pecorridos pela cobra
    window.fill(PRETO) # A cor deve ser a mesma do fundo da tela!

    
    # Cobra e comida
    cobra = pygame.draw.rect(window, VERDE, (x, y, 10, 10))
    comida = pygame.draw.rect(window, VERMELHO, (x_comida, y_comida, 20, 20)) 

    # Cobra comendo a comida
    if cobra.colliderect(comida):
        x_comida = randint(0, 600) 
        y_comida = randint(0, 600)

    # Fazendo a cobra retornar ao lado oposto quando chegar aos extremos
    if y >=  altura:
        y = 0
    elif y <= 0:
        y = altura        
    if x >= largura:
        x = 0
    elif x <= 0:
        x = largura


    pygame.display.update()


pygame.quit()