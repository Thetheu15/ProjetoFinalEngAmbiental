import pygame

class Text:
    def __init__(self, position, text, font_size=36, color=(0, 0, 0)):
        self.position     = position
        self.text         = text
        self.color        = color
        self.font         = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, color)
        self.text_rect    = self.text_surface.get_rect(topleft=self.position)

    def draw(self, screen):
        screen.blit(self.text_surface, self.text_rect)

    def update_text(self, new_text):
        self.text         = new_text
        self.text_surface = self.font.render(new_text, True, self.color)
        self.text_rect = self.text_surface.get_rect(topleft=self.position)
