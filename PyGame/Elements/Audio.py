import pygame

class Audio:
    def __init__(self, audio_path):
        pygame.mixer.init()  # Inicializa o mixer do Pygame
        self.audio_path = audio_path
        self.is_playing = False
        pygame.mixer.music.load(audio_path)

    def play(self, loop=False):
        """Reproduz o áudio. Se loop=True, ele toca indefinidamente."""
        pygame.mixer.music.play(-1 if loop else 0)
        self.is_playing = True

    def pause(self):
        """Pausa o áudio."""
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False

    def resume(self):
        """Retoma o áudio pausado."""
        pygame.mixer.music.unpause()
        self.is_playing = True

    def stop(self):
        """Para a reprodução do áudio."""
        pygame.mixer.music.stop()
        self.is_playing = False

    def set_volume(self, volume):
        """Define o volume do áudio (valor entre 0.0 e 1.0)."""
        pygame.mixer.music.set_volume(volume)
