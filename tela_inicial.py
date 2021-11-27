import pygame, sys, random
from pygame.constants import KEYDOWN
from pygame.locals import *
from config import *
import sprites
from os import *
from pygame.math import *


class Game:
    def __init__(self):
        # Criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.window = pygame.display.set_mode(MEDIDAS_TELA)
        pygame.display.set_caption(TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.roda_jogo = True
        self.fonte = pygame.font.match_font(FONTE)
    
    
    def novo_jogo(self):
        # Mexe nas sprites do jogo
        self.all_sprites = pygame.sprite.Group()
        self.rodar()
    
    
    def rodar(self):
        # While true do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(FPS) 
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    
    def eventos(self):
        # Define eventos no game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando == False
                self.roda_jogo == False


    def atualizar_sprites(self):
        # Atualiza as sprites
        self.all_sprites.update()

    
    def desenhar_sprites(self):
        # Desenha todas as sprites
        self.window.fill(PRETO)
        self.all_sprites.draw(self.window)
        pygame.display.flip()


    def carregar_arquivos(self):
        # Carrega os arquivos (áudio, imagem,)    
        diretorio_imagem = path.join(getcwd(), 'imagens')
        self.diretorio_audios = path.join(getcwd(), 'musica_sons') # '../' retorna uma pasta anterior fora da pasta atual
        self.spritesheet = path.join(diretorio_imagem, SPRITESHEET)
        self.pacsnake_logo = path.join(diretorio_imagem, PACSNAKE_LOGO)
        self.pacsnake_logo = pygame.image.load(self.pacsnake_logo).convert() # Modificando o valor do atributo de str para imagem no pygame


    def mostrar_texto(self, mensagem, tamanho, cor, x, y):
        # Exibe um texto na tela do jogo
        fonte = pygame.font.Font(self.fonte, tamanho)
        mensagem = fonte.render(mensagem, True, cor)
        mensagem_rect = mensagem.get_rect()
        mensagem_rect.midtop = (x, y)       # Posiciona o texto nas coordenadas: (x, y)
        self.window.blit(mensagem, mensagem_rect)


    def mostrar_logo_inicio(self, x, y):
        start_logo_rect = self.pacsnake_logo.get_rect()
        start_logo_rect.midtop = (x, y)
        img = pygame.transform.scale(self.pacsnake_logo, (LARGURA - 100, 300))
        self.window.blit(img, (50, 0))


    def mostrar_tela_inicio(self):
        pygame.mixer.music.load(path.join(self.diretorio_audios, SOM_INICIO))
        pygame.mixer.music.play()

        self.mostrar_logo_inicio(LARGURA / 2, 20)

        self.mostrar_texto('- Pressione algum botão para jogar -', 
                            35, 
                            AMARELO,
                            LARGURA / 2,
                            400
                        )
        self.mostrar_texto('Desenvolvido por Cleilton, Matheus e Tales.', 
                            15, 
                            BRANCO,
                            LARGURA / 2,
                            680
                        )
        
        pygame.display.flip()
        self.esperar_por_jogador()

    
    def musica_jogo(self):
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.load(path.join(self.diretorio_audios, SOM_JOGO))
        pygame.mixer.music.play(-1)    

    
    def esperar_por_jogador(self):          # Espera até o jogador apertar a tecla para iniciar o jogo
        esperando = True
        while esperando:
            self.relogio.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.roda_jogo = False
                if event.type == pygame.KEYUP:
                    esperando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(path.join(self.diretorio_audios, TECLA_INICIO)).play()
    

    def update(self):
        self.cobra.movimento_cobra()
        self.colisao()

    
    def desenha_elementos(self):
        self.comida.desenhar_comida()
        self.cobra.desenhar_cobra()


    # Problema na colisão
    def colisao(self):
        if self.comida.pos == self.cobra.corpo[0]: 
            self.comida.aleatorio()
            # self.cobra.adicionar_bloco()


    def mostrar_tela_fim_de_jogo(self):
        pass


g = Game()
comida = Comida()
tempo = pygame.time.Clock()    
cobra = Cobra()
ATUALIZA_TELA = pygame.USEREVENT # Modifica algum evento no jogo
pygame.time.set_timer(ATUALIZA_TELA, 10)  #Velocidade constante da cobra

# Inicia a tela e, após o usuário apertar uma tecla, entra na tela principal do jogo tocando a música
g.mostrar_tela_inicio()
pygame.display.update()

g.musica_jogo() 


jogo_principal = Game()


while g.roda_jogo:
    for event in pygame.event.get():          
        if event.type == pygame.QUIT:           # Fecha a janela do jogo quando aperta no 'X' da tela
            g.roda_jogo = False
        if event.type == ATUALIZA_TELA:
            jogo_principal.update()
        if event.type == KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                jogo_principal.cobra.direcao = Vector2(0, -2)
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                jogo_principal.cobra.direcao = Vector2(0, 2)
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                jogo_principal.cobra.direcao = Vector2(2, 0)
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                jogo_principal.cobra.direcao = Vector2(-2, 0)


       
    JANELA.fill(PRETO)
    jogo_principal.desenha_elementos()
    pygame.display.update()
    tempo.tick(60)
