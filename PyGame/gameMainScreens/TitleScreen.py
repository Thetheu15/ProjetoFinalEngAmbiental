from Classes.Button import Button
from Classes.Screen import RootScreen

class TitleScreen:
    def __init__(self, width, height, background_color):
        self.screen = RootScreen(width, height, background_color)
        self.button = Button((175, 225), 150, 50, "Clique Aqui")
    
    def draw(self):
        self.screen.draw_background()
        self.button.draw(self.screen.screen)
    
    def handle_event(self, event):
        if self.button.is_clicked(event):
            print("Botão clicado!")
