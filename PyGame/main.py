import pygame
from gameMainScreens.TitleScreen import TitleScreen
from gameMainScreens.MainMapScreen import MapScreen
import time

# Inicializa o Pygame
pygame.init()
clock = pygame.time.Clock()

mapScreen   = MapScreen(width  = 600,
                        height = 600)

titleScreen = TitleScreen(width = 720,
                          height= 600)

actualScreen = "titleScreen"

running = True
while running:
    dt = clock.tick(60)  
    
    if actualScreen == "titleScreen":
        titleScreen.draw()
    elif actualScreen == "mapScreen":
        mapScreen.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if actualScreen == "titleScreen":
            actualScreen = titleScreen.handleEvent(event)
        elif actualScreen == "mapScreen":
            actualScreen = mapScreen.handleEvent(event)
    
    pygame.display.flip()

pygame.quit()
