import pygame
import random
##from config import **,**,**,**,**
##from tela_do_jogo import *jogo*
##form init/end _screen import tela inicial e final

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((0,0)) ##subistituir dps 0 pelo valor correto
pygame.display.set_caption('nome do jogo') ## adicionar nome do jogo depois

state = True
while state != False:
    if state == True:
        state = 1
    elif state == 1:
        state = [0,'x']
    else:
        state = False

pygame.quit()