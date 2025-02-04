import pygame
from gameMainScreens.TitleScreen import TitleScreen
from gameMainScreens.MainMapScreen import MainMapScreen
import time

# Inicializa o Pygame
pygame.init()

mapScreen   = MainMapScreen()
titleScreen = TitleScreen(1024,720)

is_title = True

running = True
while running:
    if is_title:
        titleScreen.draw()
    else:
        mapScreen.draw()
        map = True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if is_title:
            is_title = titleScreen.handle_event(event)
    
    pygame.display.flip()

pygame.quit()
