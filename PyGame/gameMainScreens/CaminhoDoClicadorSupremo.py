from Elements.Button import Button
from Elements.Screen import RootScreen
import pygame
import time

class ResenhaScreen:
    def __init__(self, width, height, background_color):
        self.screen = RootScreen(width, height, background_color)
        self.button = Button((175, 225), 150, 50, "Clique Aqui")
        self.i = 0

    def draw(self):
        self.screen.draw_background()
        self.button.draw(self.screen.screen)
    
    def handle_event(self, event):
        if self.button.is_clicked(event):
            self.i = self.i + 1
            if(self.i == 1):
                print("Botão clicado 1 vez!")
            elif(self.i < 100):
                print("Botão clicado", self.i, " vezes!")
            elif(self.i < 200):
                print("Botão clicado", self.i, " vezes! Está tudo bem com você?")
            elif(self.i < 1000):
                print("Botão clicado ", self.i, " vezes! Você TEM certeza estar bem?")
            else:
                print("\n\nWOW!!! Você é o Clicador Supremo! Como se sente tendo pertido tanto tempo apertando um botão?")
                print("Em prol da tua sanidade mental, o jogo será fechado imediatamente!\n\n\n")
                time.sleep(2)
                pygame.quit()
