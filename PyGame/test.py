import pygame
import time

# Inicializa o Pygame
pygame.init()

# Configuração da tela
largura, altura = 500, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Fade Out de Imagem")

# Carregar imagem e converter para suportar transparência
imagem = pygame.image.load("Images/playerBack.png").convert_alpha()

# Posição da imagem
pos_x, pos_y = 100, 50

# Definir opacidade inicial
alpha = 255
imagem.set_alpha(alpha)

rodando = True
while rodando:
    tela.fill((30, 30, 30))  # Fundo escuro

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Reduz a opacidade aos poucos
    if alpha > 0:
        alpha -= 2  # Ajuste esse valor para mudar a velocidade do fade
        imagem.set_alpha(alpha)

    # Desenha a imagem na tela
    tela.blit(imagem, (pos_x, pos_y))

    pygame.display.flip()
    time.sleep(0.02)  # Pequeno delay para suavizar o efeito

pygame.quit()
