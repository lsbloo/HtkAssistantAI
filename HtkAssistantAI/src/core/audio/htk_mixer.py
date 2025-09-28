
import pygame

class HtkAudioMixer:
    def __init__(self, logger=None):
        pygame.mixer.init()
        self.logger = logger
        self.logger.log("HtkAudioMixer initialized.")

    def play_audio(self, file_path):
        try:
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            self.logger.log(f"Playing audio file: {file_path}")
            
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
            
            self.stop_audio()
            
        except Exception as e:
            self.logger.log(f"Error playing audio file {file_path}: {e}")

    def stop_audio(self):
        pygame.mixer.music.stop()
        self.logger.log("Audio playback stopped.")
        pygame.mixer.quit()
        self.logger.log("Audio playback finished.")
        