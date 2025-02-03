import pygame

class Button:
    def __init__(self, initPoint, width, height, text, font_size=36, color=(0, 0, 255), hover_color=(0, 0, 180), text_color=(255, 255, 255)):
        self.rect         = pygame.Rect(initPoint[0], initPoint[1], width, height)
        self.color        = color
        self.hover_color  = hover_color
        self.text         = text
        self.text_color   = text_color
        self.font         = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect    = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color     = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        
        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)