import pygame

# Inicializa o Pygame
pygame.init()

# Configuração da tela
largura, altura = 500, 300
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Barra de Vida no Pygame")

# Definições da barra de vida
vida_max = 300
vida_atual = vida_max
barra_pos = (50, 100, 300, 30)  # (x, y, largura, altura)
cor_fundo = (50, 50, 50)  # Cinza escuro (fundo da barra)
cor_vida = (0, 255, 0)  # Verde (vida cheia)
cor_dano = (255, 0, 0)  # Vermelho (para efeito de dano)

healthDownCounter = 60
postDamageCounter = 60
countDamageTaken = 0
damageTaken = False
clock = pygame.time.Clock()
# Loop principal
rodando = True
while rodando:
    dt = clock.tick(60)  
    tela.fill((255, 255, 255))  # Fundo da tela

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

        # Reduz a vida ao pressionar espaço
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                damageTaken = True
                countDamageTaken += 1
                # vida_atual -= 10  # Simula dano
                vida_atual = max(0, vida_atual)
    if healthDownCounter > 0 and damageTaken == True:
        vida_atual -= 1.6667

        pygame.draw.rect(tela, cor_fundo, barra_pos)

        pygame.draw.rect(tela, cor_vida, (barra_pos[0], barra_pos[1], (vida_atual+60 if vida_atual < vida_max-100*countDamageTaken+40 else vida_max-100*(countDamageTaken-1)), barra_pos[3]))
        pygame.draw.rect(tela, cor_dano, (barra_pos[0], barra_pos[1], vida_atual, barra_pos[3]))
        healthDownCounter -= 1

    elif healthDownCounter == 0:
        pygame.draw.rect(tela, cor_fundo, barra_pos)

        pygame.draw.rect(tela, cor_vida, (barra_pos[0], barra_pos[1], vida_atual+postDamageCounter, barra_pos[3]))
        pygame.draw.rect(tela, cor_dano, (barra_pos[0], barra_pos[1], vida_atual, barra_pos[3]))
        postDamageCounter -= 1
        if (postDamageCounter == 0):
            healthDownCounter = 60
            postDamageCounter = 60
            damageTaken = False

    elif damageTaken == False:
        vida_atual = (vida_atual / vida_max) * barra_pos[2] 

        pygame.draw.rect(tela, cor_fundo, barra_pos)
        pygame.draw.rect(tela, cor_vida, (barra_pos[0], barra_pos[1], vida_atual, barra_pos[3]))

    pygame.display.flip()  # Atualiza a tela

pygame.quit()
