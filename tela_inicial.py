import pygame
from config import *
import sprites
from os import *


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
        self.carregar_arquivos()
    
    
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
        self.all_sprites.updates()

    
    def desenhar_sprites(self):
        # Desenha todas as sprites
        self.window.fill(PRETO)
        self.all_sprites.draw(self.window)
        pygame.display.flip()


    def carregar_arquivos(self):
        # Carrega os arquivos (áudio, imagem,)    
        diretorio_imagem = path.join('../', 'imagens')
        self.diretorio_audios = path.join('../', 'musica_sons') # '../' retorna uma pasta anterior fora da pasta atual
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

        self.mostrar_texto('-Pressione algum botão para jogar-', 
                            35, 
                            AMARELO,
                            LARGURA / 2,
                            320
                        )
        self.mostrar_texto('Desenvolvido por Cleilton, Matheus, Tales', 
                            15, 
                            BRANCO,
                            LARGURA / 2,
                            680
                        )
        
        pygame.display.flip()
        self.esperar_por_jogador()

    
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

    def mostrar_tela_fim_de_jogo(self):
        pass


g = Game()
g.mostrar_tela_inicio()


while g.roda_jogo:
    g.novo_jogo()
    g.mostrar_tela_fim_de_jogo()