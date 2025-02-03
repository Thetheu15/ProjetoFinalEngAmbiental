from Elements.Screen import RootScreen
from Elements.Image import Image

class MainMapScreen:
    def __init__(self, width=500, height=500, background_color=(255,255,255)):
        self.screen = RootScreen(width, height, background_color)
        self.image  = Image("Images/teste.png", (width // 2 - 77, height // 2 - 74))
    
    def draw(self):
        self.screen.draw_background()
        self.image.draw(self.screen.screen)
        