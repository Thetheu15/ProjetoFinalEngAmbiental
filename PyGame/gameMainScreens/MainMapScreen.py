import pygame
from Elements.Screen import Screen
from Elements.Image import Image

class MapScreen:
    def __init__(self, width=500, height=500, background_color=(255,255,255)):
        self.screen = Screen(width, height, background_color)
        self.image  = Image("Images/teste.png", (width // 2 - 77, height // 2 - 74))
    
    def draw(self):
        self.screen.draw_background()
        self.image.draw(self.screen.screen)

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_k:
            return "titleScreen"
        else:
            return "mapScreen"
        # elif event.type == pygame.KEYUP and event.key == pygame.K_k:
        #     self.k_pressed = False

