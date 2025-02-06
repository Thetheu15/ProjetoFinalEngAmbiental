import pygame

IMAGE_HEIGHT = 0
IMAGE_WIDTH  = 0

class Image:
    def __init__(self, image_path, position, spriteRows = 0, spriteColumns = 0, animationSlowness = 0):
        global IMAGE_HEIGHT, IMAGE_WIDTH

        self.image         = pygame.image.load(image_path).convert_alpha()
        self.rect          = self.image.get_rect(topleft=position)
        self.spriteRows    = spriteRows
        self.spriteColumns = spriteColumns

        self.animationRows    = 0
        self.animationColumns = 0

        self.framesFrozen      = animationSlowness
        self.animationSlowness = animationSlowness

        self.Height = self.image.get_height()
        self.widht  = self.image.get_width()

    def draw(self, screen, slice=None):
        if slice == None: screen.blit(self.image, self.rect, (0, 0, self.widht, self.Height))
        else:             screen.blit(self.image, self.rect, slice)
    
    def update_position(self, new_position):
        self.rect.topleft = new_position

    def showFrame(self, screen):
        screen.blit(self.image, self.rect, (self.animationColumns*self.widht//self.spriteColumns, 
                                            self.animationRows*self.Height//self.spriteRows, 
                                            self.widht//self.spriteColumns, self.Height//self.spriteRows))
    
    def updateFrame(self, screen):
        if self.framesFrozen == 0:
            self.framesFrozen = self.animationSlowness

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
            self.showFrame(screen)
            self.framesFrozen -= 1
        
