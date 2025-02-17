import pygame
import time

class Text:
    def __init__(self, position, text, font_size=36, color=(0, 0, 0), speed=0.05, max_chars_per_line=30):
        self.position = position
        self.max_chars_per_line = max_chars_per_line
        self.full_text = self.format_text(text, max_chars_per_line)
        self.current_text = ""
        self.color = color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render("", True, color)
        self.text_rect = self.text_surface.get_rect(topleft=self.position)
        self.color = color
        self.index = 0
        self.speed = speed
        self.last_time = time.time()
        self.finished = False

    def format_text(self, text, max_chars_per_line):
        words = text.split()
        formatted_text = ""
        line = ""
        for word in words:
            if len(line) + len(word) + 1 > max_chars_per_line:
                formatted_text += line.strip() + "\n"
                line = ""
            line += word + " "
        formatted_text += line.strip()
        return formatted_text

    def changeText(self, text):
        self.full_text = self.format_text(text, self.max_chars_per_line)
        self.text_surface = self.font.render("", True, self.color)
        self.text_rect = self.text_surface.get_rect(topleft=self.position)

    def update(self):
        if not self.finished and self.index < len(self.full_text):
            if time.time() - self.last_time > self.speed:
                self.current_text = self.full_text[:self.index + 1]
                self.index += 1
                self.last_time = time.time()
                self.text_surface = self.font.render(self.current_text, True, self.color)
                self.text_rect = self.text_surface.get_rect(topleft=self.position)
        else:
            self.finished = True
    
    def resetText(self):
        self.index    = 0
        self.finished = False

    def draw(self, screen):
        self.update()

        y_offset = 0
        for line in self.current_text.split("\n"):
            line_surface = self.font.render(line, True, self.color)
            line_rect    = line_surface.get_rect(topleft=(self.position[0], self.position[1] + y_offset))
            y_offset    += self.font.get_height()
            screen.blit(line_surface, line_rect)