from Elements.Button import Button
from Elements.Screen import RootScreen
from Elements.Text   import Text
from Elements.Audio  import Audio
from Elements.Image  import Image

class TitleScreen:
    def __init__(self, width=500, height=500, background_color=(255,255,255)):
        self.screen = RootScreen(width, height, background_color)
        self.button = Button((175, 225), 150, 50, "Clique Aqui")
        self.title  = Text((50,50), "Hello World")
        self.image  = Image("Sprites/sprite1.png", (0,0))
        self.music  = Audio("Audios/music.mp3") 

        self.music.play()
        
    
    def draw(self):
        self.screen.draw_background()
        self.image.draw(self.screen.screen, (0,0,500,500))
        # self.button.draw(self.screen.screen)
        # self.title.draw(self.screen.screen)

    
    def handle_event(self, event):
        if self.button.is_clicked(event):
            print("Botão clicado!")
            return False
        else:
            return True