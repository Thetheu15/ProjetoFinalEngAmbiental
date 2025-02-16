import pygame
from gameMainScreens.BossScreen import BossScreen

pygame.init()
clock = pygame.time.Clock()

bossScreen  = BossScreen(width = 1600,
                        height = 900)

actualScreen = "bossScreen"

running = True
while running:
    dt = clock.tick(60)  
    bossScreen.draw()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if actualScreen == "bossScreen":
            bossScreen.handleEvent(event)

    
    pygame.display.flip()

pygame.quit()
