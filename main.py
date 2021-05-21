import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.10)
musica_de_fundo = pygame.mixer.music.load("Sons/BoxCat Games - B-3.mp3")
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound("Sons/smw_coin.wav")
barulho_colisao.set_volume(0.30)

LARGURA = 640
ALTURA = 480
x = int((LARGURA / 2) - (40 / 2))
y = int((ALTURA / 2 ) - (50 / 2))

x_azul = randint(40, 600)
y_azul = randint(50, 430)

FONTE = pygame.font.SysFont("arial", 40, True, True)
pontos = 0

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo")
relogio = pygame.time.Clock()
while True:
    relogio.tick(60)
    tela.fill((0, 0, 0))
    mensagem = f"Pontos: {pontos}"
    texto_formatado = FONTE.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        """if event.type == KEYDOWN:
            if event.key == K_a:
                x -= 20
            elif event.key == K_d:
                x += 20
            if event.key == K_w:
                y -= 20
            elif event.key == K_s:
                y +=    20"""

        if event.type == QUIT:
            pygame.quit()
            exit()
    if pygame.key.get_pressed()[K_a]:
        x -= 10
    elif pygame.key.get_pressed()[K_d]:
        x += 10
    if pygame.key.get_pressed()[K_w]:
        y -= 10
    elif pygame.key.get_pressed()[K_s]:
        y += 10

    rect_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))
    rect_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))

    if rect_vermelho.colliderect(rect_azul):
        pontos += 1
        barulho_colisao.play()
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)

    #pygame.draw.circle(tela, (0, 0, 120), (300, 260), 40)
    '''Retangulo: Local onde será desenhado, cor, posição junto da largura e altura.'''
    '''Circulo: Local onde será desenhado, cor, posição, raio.'''
    #pygame.draw.line(tela, (255, 255, 0), (390, 0), (390, 600), 5)
    '''Linha: Local onde será desenhado, cor, posição inicial, posição final e espessura.'''

    tela.blit(texto_formatado, (425, 20))
    pygame.display.update()
