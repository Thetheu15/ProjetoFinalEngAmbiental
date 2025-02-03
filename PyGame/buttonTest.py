from imports import *
from Classes.Button import Button
from Classes.Screen import RootScreen

# Inicializa o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 500, 500

# Definição de cores
WHITE = (255, 255, 255)

# Criando o botão
button = Button((50,100), 150, 50, "Clique Aqui")
rootScreen = RootScreen(500, 500, (255, 255, 255))

#Loop principal do game
running = True
while running:
    rootScreen.draw_background()

    button.draw(rootScreen.screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif button.is_clicked(event):
            print("Botão clicado!")

    pygame.display.flip()

pygame.quit()
