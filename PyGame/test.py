import pygame

# Inicializa o Pygame
pygame.init()

# Configuração da tela
largura, altura = 500, 500
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Botão com Imagem no Pygame")

# Carregar a imagem do botão
botao_img = pygame.image.load("botao.png")  # Substitua pelo nome do seu arquivo
botao_rect = botao_img.get_rect(topleft=(150, 200))  # Define a posição do botão

# Função que será chamada ao clicar no botão
def clique_no_botao():
    print("Botão clicado!")

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Verifica se o botão foi clicado
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if botao_rect.collidepoint(evento.pos):
                clique_no_botao()

    # Desenha o botão na tela
    tela.fill((30, 30, 30))  # Cor de fundo
    tela.blit(botao_img, botao_rect.topleft)

    pygame.display.flip()  # Atualiza a tela

pygame.quit()
