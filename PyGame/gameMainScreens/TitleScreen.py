from Elements.Button import Button
from Elements.Screen import Screen
from Elements.Text   import Text
from Elements.Audio  import Audio
from Elements.Image  import Image

class TitleScreen:
    def __init__(self, width=500, height=500, background_color=(200,100,50)):
        self.screen = Screen(width, height, background_color)

        self.button = Button(position= (300, 300), 
                             width    = 150, 
                             height   = 50, 
                             text     = "Clique Aqui")
        
        self.title  = Text(position= (50,50), 
                           text    = "Hello World")

        self.animation1  = Image("Sprites/sprite1.png", 
                                  position     =(0,0), 
                                  spriteRows   =5, 
                                  spriteColumns=5,
                                  animationSlowness=5)

        self.music  = Audio("Audios/music.mp3")
        self.music.play()
        
    def draw(self):
        self.screen.draw_background()
        self.animation1.updateFrame(self.screen.screen) 
        self.button.draw(self.screen.screen)

        # self.image.draw(self.screen.screen)
        # self.title.draw(self.screen.screen)

    
    def handleEvent(self, event):
        if self.button.is_clicked(event):
            print("Botão clicado!")
            return "mapScreen"
        else:
            return "titleScreen"