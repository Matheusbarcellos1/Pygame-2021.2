import pygame
from random import randint
from config import PRETO, VERMELHO, VERDE, BRANCO, AZUL
from config import medidas_tela, x, y, vel_cobra, largura, altura, pontos


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

# Pontos
pontos = 0

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
        if event.type == pygame.QUIT:           #fecha a janela do jogo quando aperta no 'X' da tela
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

    # Marcador de pontos
    fonte = pygame.font.Font(None, 48)
    marcador_pontos = fonte.render(f'Pontos: {pontos}', True, VERMELHO) # Pontos com fonte
    window.blit(marcador_pontos, [0, 0])

    
    # Cobra e comida
    cobra = pygame.draw.rect(window, VERDE, (x, y, 10, 10))
    comida = pygame.draw.rect(window, VERMELHO, (x_comida, y_comida, 20, 20)) 

    # Cobra comendo a comida
    if cobra.colliderect(comida):
        x_comida = randint(0, 600) 
        y_comida = randint(0, 600)
        pontos += 1
        barulho_comendo.play()


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