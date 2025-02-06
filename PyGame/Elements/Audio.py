import pygame

class Audio:
    def __init__(self, audio_path):
        pygame.mixer.init()  # Inicializa o mixer
        self.audio = pygame.mixer.Sound(audio_path)  # Usa Sound em vez de music
        
        self.channel = None  # Canal onde o som será tocado
        self.is_playing = False

    def play(self, loop=False):
        """Reproduz o áudio. Se loop=True, ele toca indefinidamente."""
        self.channel = self.audio.play(-1 if loop else 0)  # Toca o som
        self.is_playing = True

    def pause(self):
        """Pausa o áudio."""
        if self.channel and self.is_playing:
            self.channel.pause()
            self.is_playing = False

    def resume(self):
        """Retoma o áudio pausado."""
        if self.channel:
            self.channel.unpause()
            self.is_playing = True

    def stop(self):
        """Para a reprodução do áudio."""
        if self.channel:
            self.channel.stop()
            self.is_playing = False

    def set_volume(self, volume):
        """Define o volume do áudio (valor entre 0.0 e 1.0)."""
        self.audio.set_volume(volume)
