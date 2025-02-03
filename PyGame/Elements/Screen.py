import pygame

class RootScreen:
    def __init__(self, width=500, height=500, background_color=(255,255,255)):
        self.width            = width
        self.height           = height
        self.background_color = background_color
        self.screen           = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Jogo 2D")
    
    def draw_background(self):
        self.screen.fill(self.background_color)