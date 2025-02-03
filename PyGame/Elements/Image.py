import pygame

class Image:
    def __init__(self, image_path, position):
        self.image_path = image_path
        self.image = pygame.image.load(image_path).convert()
        self.rect = self.image.get_rect(topleft=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_position(self, new_position):
        self.rect.topleft = new_position