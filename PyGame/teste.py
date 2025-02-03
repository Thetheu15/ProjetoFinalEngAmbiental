import pygame
from gameMainScreens.TitleScreen import TitleScreen

# Inicializa o Pygame
pygame.init()

game_screen = TitleScreen(500, 500, (255, 255, 255))

running = True
while running:
    game_screen.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game_screen.handle_event(event)
    
    pygame.display.flip()

pygame.quit()
