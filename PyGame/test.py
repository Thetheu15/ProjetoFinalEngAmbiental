import pygame

IMAGE_HEIGHT = 0
IMAGE_WIDTH  = 0

class Image:
    def __init__(self, image_path, position, spriteRows=0, spriteColumns=0, animationSlowness=0):
        global IMAGE_HEIGHT, IMAGE_WIDTH

        # Usando convert_alpha() para manter a transparência
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect  = self.image.get_rect(topleft=position)
        self.spriteRows    = spriteRows
        self.spriteColumns = spriteColumns

        self.animationRows    = 0
        self.animationColumns = 0

        self.framesFrozen      = animationSlowness
        self.animationSlowness = animationSlowness

        IMAGE_HEIGHT = self.image.get_height()
        IMAGE_WIDTH  = self.image.get_width()

    def draw(self, screen, slice=None):
        global IMAGE_HEIGHT, IMAGE_WIDTH
        if slice is None:
            screen.blit(self.image, self.rect, (0, 0, IMAGE_WIDTH, IMAGE_HEIGHT))
        else:
            screen.blit(self.image, self.rect, slice)
    
    def update_position(self, new_position):
        self.rect.topleft = new_position

    def showFrame(self, screen):
        # Calcula a fatia a ser desenhada com base no frame atual
        slice_rect = (self.animationColumns * IMAGE_WIDTH // 5, 
                      self.animationRows * IMAGE_HEIGHT // 5, 
                      IMAGE_WIDTH // 5, IMAGE_HEIGHT // 5)
        screen.blit(self.image, self.rect, slice_rect)
    
    def updateFrame(self, screen):
        if self.framesFrozen == 0:
            self.framesFrozen = self.animationSlowness
            if self.animationRows < self.spriteRows:
                if self.animationColumns < self.spriteColumns:
                    self.showFrame(screen)
                    self.animationColumns += 1
                else: 
                    self.animationColumns = 0
                    self.animationRows   += 1
                    self.showFrame(screen)
                    self.animationColumns += 1
            else:
                self.animationColumns = 0
                self.animationRows    = 0  
                self.showFrame(screen)
                self.animationColumns += 1
        else: 
            self.showFrame(screen)
            self.framesFrozen -= 1

# Exemplo de uso no loop principal:
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Animação com Transparência")

# Supondo que 'sprite.png' seja uma spritesheet com fundo transparente
anim_image = Image("Sprites/sprite1.png", (100, 100), spriteRows=5, spriteColumns=5, animationSlowness=5)

clock = pygame.time.Clock()
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Limpa a tela (desenha o fundo)
    screen.fill((255, 255, 255))  # Fundo preto, por exemplo

    # Atualiza a animação
    anim_image.updateFrame(screen)
    
    # Atualiza a tela
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
