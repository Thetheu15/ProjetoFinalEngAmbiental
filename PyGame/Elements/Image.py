import pygame

IMAGE_HEIGHT = 0
IMAGE_WIDTH  = 0

class Image:
    def __init__(self, image_path, position, spriteRows = 0, spriteColumns = 0, animationSlowness = 0):
        global IMAGE_HEIGHT, IMAGE_WIDTH

        self.position      = position
        self.image         = pygame.image.load(image_path).convert_alpha()
        self.rect          = self.image.get_rect(topleft=position)
        self.spriteRows    = spriteRows
        self.spriteColumns = spriteColumns
        self.totalNumFrames = spriteColumns * spriteRows * (animationSlowness if animationSlowness != 0 else 1) 
        self.animationRows    = 0
        self.animationColumns = 0

        self.framesFrozen      = animationSlowness
        self.animationSlowness = animationSlowness

        self.Height = self.image.get_height()
        self.widht  = self.image.get_width()

        self.alpha = 255

    def scale(self, scale):
        self.image = pygame.transform.scale(self.image, scale)
        self.rect  = self.image.get_rect(topleft=self.position)
        self.Height = scale[0]
        self.widht = scale[1]

    def draw(self, screen, slice=None):
        if slice == None: screen.blit(self.image, self.rect)
        else:             screen.blit(self.image, self.rect, slice)
    
    def update_position(self, new_position):
        self.rect.topleft = new_position

    def resetAnimation(self):
        self.animationColumns = 0
        self.animationRows = 0

    def showFrame(self, screen):
        screen.blit(self.image, self.rect, (self.animationColumns*self.widht//self.spriteColumns, 
                                            self.animationRows*self.Height//self.spriteRows, 
                                            self.widht//self.spriteColumns, self.Height//self.spriteRows))
        
    def fadeImageAnimation(self, screen, timeToFade, is_animation=False):
        self.image.set_alpha(self.alpha)
        
        if (is_animation == True): self.showFrame(screen)
        else:                      self.draw(screen)
        
        self.alpha -= 2
    
    def doAnimation(self, screen):
        
        if self.framesFrozen == 0:
            self.framesFrozen = self.animationSlowness
            self.showFrame(screen)

            if self.animationRows < self.spriteRows:
                if self.animationColumns < self.spriteColumns-1:
                    self.showFrame(screen)
                    self.animationColumns += 1
             
                else: 
                    self.animationColumns = 0
                    self.animationRows   += 1 
                    self.showFrame(screen)
            else:
                self.animationColumns = 0
                self.animationRows    = 0  
                self.showFrame(screen)

        else: 
            if self.animationRows == self.spriteRows and self.animationColumns == 0: 
                self.animationRows    -= 1
                self.animationColumns += 1
                
                self.showFrame(screen)

                self.animationRows    = 0
                self.animationColumns = 0

                self.framesFrozen -= 1
                return 

            else:
                self.showFrame(screen)
                self.framesFrozen -= 1

            
        
        
