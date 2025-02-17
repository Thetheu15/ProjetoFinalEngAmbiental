import pygame

class Button:
    def __init__(self, screen, position, width, height, text, font_size=36, color=(0, 0, 255), hover_color=(255, 255, 255), text_color=(255, 255, 255)):
        self.screen       = screen
        self.rect         = pygame.Rect(position[0], position[1], width, height)
        self.rect1        = pygame.Rect(position[0]+5, position[1]+5, width-10, height-10)
        self.color        = color
        self.color1       = (0,0,50)
        self.hover_color  = hover_color
        self.text         = text
        self.text_color   = text_color
        self.font         = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect    = self.text_surface.get_rect(center=self.rect.center)
        self.text_color   = text_color
        self.isCorrectAnswer = False

    def draw(self, text=''):
        mouse_pos = pygame.mouse.get_pos()
        color     = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        self.changeText(text)
        
        pygame.draw.rect(self.screen, color, self.rect, border_radius=0)
        pygame.draw.rect(self.screen, self.color1, self.rect1, border_radius=0)
        self.screen.blit(self.text_surface, self.text_rect)
    
    def changeText(self, text):
        self.text = text
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.text_rect    = self.text_surface.get_rect(center=self.rect.center)
    
    def changeCorrectAnswerState(self, state):
        self.isCorrectAnswer = state

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)