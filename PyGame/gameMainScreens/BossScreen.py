from Elements.Button import Button
from Elements.Screen import Screen
from Elements.Text   import Text
from Elements.Audio  import Audio
from Elements.Image  import Image
import pygame

class BossScreen:
    def __init__(self, width=500, height=500, background_color=(200,100,50)):
        self.background_color = background_color

        self.mainScreen = Screen(width, height, background_color)

        self.boss       = Image('Sprites/bossAnim.png',
                                position          = (1100,50), 
                                spriteRows        = 2, 
                                spriteColumns     = 3,
                                animationSlowness = 6)
        self.boss.scale((700,700))

        self.player    = Image('Images/playerBack.png', (200, 225))
        self.player.scale((300,300))

        self.hitAnim    = Image('Sprites/hit1.png',
                                position          = (0,0), 
                                spriteRows        = 4, 
                                spriteColumns     = 4,
                                animationSlowness = 12)
        
        self.option1    = Button((500,600), 300, 150, "text")
        self.option2    = Button((750,700), 300, 50, "text")
        self.option3    = Button((450,800), 300, 50, "text")
        self.option4    = Button((750,800), 300, 50, "text")

        self.hitAnim_trigger = False 
        self.countFrame = 0


    def draw(self):
        self.mainScreen.draw_background()
        pygame.draw.line(self.mainScreen.screen, (255, 255, 255), (0, 600), (1600, 600), 5)
        pygame.draw.line(self.mainScreen.screen, (255, 255, 255), (800, 0), (800, 900), 1)
        pygame.draw.line(self.mainScreen.screen, (255, 255, 255), (0, 450), (1600, 450), 1)
        pygame.draw.ellipse(self.mainScreen.screen, (0, 0, 0), (1010, 310, 400, 150))
        pygame.draw.ellipse(self.mainScreen.screen, (0, 0, 0), (170, 470, 350, 100))

        self.boss.updateFrame(self.mainScreen.screen)
        self.player.draw(self.mainScreen.screen)

        self.option1.draw(self.mainScreen.screen)
        # self.option2.draw(self.mainScreen.screen)
        # self.option3.draw(self.mainScreen.screen)
        # self.option4.draw(self.mainScreen.screen)

        if self.hitAnim_trigger and self.countFrame <= self.hitAnim.totalNumFrames: 
            self.hitAnim.updateFrame(self.mainScreen.screen) 
            self.countFrame += 1
        else:
            self.hitAnim_trigger = False
            self.countFrame = 0
            self.hitAnim.resetAnimation()

    def handleEvent(self, event):
        if self.option1.is_clicked(event):
            self.hitAnim_trigger = True
        