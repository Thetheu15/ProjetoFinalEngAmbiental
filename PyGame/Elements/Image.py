import pygame
IMAGE_HEIGHT = 0
IMAGE_WIDTH  = 0

class Image:
    def __init__(self, image_path, position):
        global IMAGE_HEIGHT, IMAGE_WIDTH

        self.image_path = image_path
        self.image      = pygame.image.load(image_path).convert()
        self.rect       = self.image.get_rect(topleft=position)

        IMAGE_HEIGHT = self.image.get_height()
        IMAGE_WIDTH = self.image.get_width()

    def draw(self, screen, slice=None):
        global IMAGE_HEIGHT, IMAGE_WIDTH

        if slice == None:
            screen.blit(self.image, self.rect, (0,0, IMAGE_WIDTH, IMAGE_HEIGHT))
        else: 
            screen.blit(self.image, self.rect, slice)
            

    # def image_at(self, rectangle, colorkey = None):
    #     "Loads image from x,y,x+offset,y+offset"
    #     rect = pygame.Rect(rectangle)
    #     image = pygame.Surface(rect.size).convert()
    #     image.blit(self.sheet, (0, 0), rect)

    def update_position(self, new_position):
        self.rect.topleft = new_position