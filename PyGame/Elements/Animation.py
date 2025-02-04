import pygame

class SpriteSheet:
    def __init__(self, image_path, frame_width, frame_height, columns, rows, animation_speed=100, position=(0, 0)):
        self.spritesheet = pygame.image.load(image_path).convert_alpha()
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.columns = columns
        self.rows = rows
        self.num_frames = columns * rows
        self.frames = []
        self.current_frame = 0
        self.animation_speed = animation_speed
        self.counter = 0
        self.position = position
        
        for row in range(rows):
            for col in range(columns):
                x = col * frame_width
                y = row * frame_height
                self.frames.append(self.spritesheet.subsurface(pygame.Rect(x, y, frame_width, frame_height)))
    
    def update(self, dt):
        self.counter += dt
        if self.counter >= self.animation_speed:
            self.counter = 0
            self.current_frame = (self.current_frame + 1) % self.num_frames
    
    def draw(self, screen):
        screen.blit(self.frames[self.current_frame], self.position)
    
    def set_position(self, x, y):
        self.position = (x, y)
