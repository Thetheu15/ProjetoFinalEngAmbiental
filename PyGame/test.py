import pygame

class Screen:
    def __init__(self, width, height, background_color):
        self.width = width
        self.height = height
        self.background_color = background_color
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Jogo 2D")
    
    def draw_background(self):
        self.screen.fill(self.background_color)

class Button:
    def __init__(self, x, y, width, height, text, font_size=36, color=(0, 0, 255), hover_color=(0, 0, 180), text_color=(255, 255, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.text_surface = self.font.render(text, True, text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, color, self.rect)
        screen.blit(self.text_surface, self.text_rect)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)

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

class GameScreen:
    def __init__(self, width, height, background_color, sprite_sheet_path):
        self.screen = Screen(width, height, background_color)
        self.button = Button(175, 225, 150, 50, "Clique Aqui")
        self.sprite = SpriteSheet(sprite_sheet_path, 300, 300, 4, 4, animation_speed=80, position=(500, 500))
    
    def draw(self):
        self.screen.draw_background()
        self.button.draw(self.screen.screen)
        self.sprite.draw(self.screen.screen)
    
    def update(self, dt):
        self.sprite.update(dt)
    
    def handle_event(self, event):
        if self.button.is_clicked(event):
            print("Botão clicado!")

# Inicializa o Pygame
pygame.init()
clock = pygame.time.Clock()

game_screen = GameScreen(1000, 1000, (255, 255, 255), "Sprites/sprite1.png")  # Substitua pelo caminho correto

running = True
while running:
    dt = clock.tick(60)  # Controla a taxa de quadros e obtém o tempo decorrido
    game_screen.draw()
    game_screen.update(dt)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        game_screen.handle_event(event)
    
    pygame.display.flip()

pygame.quit()
