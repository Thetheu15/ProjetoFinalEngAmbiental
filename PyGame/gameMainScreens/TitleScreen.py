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
        self.music  = Audio("Audios/music.mp3") 
        self.image  = Image("Sprites/sprite1.png", 
                            position=(0,0), 
                            spriteRows=5, 
                            spriteColumns=5,
                            animationSlowness=10)

        self.music.play()
        
    
    def draw(self):
        self.image.updateFrame(self.screen.screen) 

        # self.screen.draw_background()
        # self.image.draw(self.screen.screen)
        # self.button.draw(self.screen.screen)
        # self.title.draw(self.screen.screen)

    
    def handle_event(self, event):
        if self.button.is_clicked(event):
            print("Botão clicado!")
            return False
        else:
            return True