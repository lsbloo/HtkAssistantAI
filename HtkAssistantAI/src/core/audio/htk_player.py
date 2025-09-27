import speech_recognition as sr
from core.log.htk_logger import HtkApplicationLogger
from core.utils.design.observer.observer import Subject
from core.utils.os_env.os_env import HtkOsEnvironment
from gtts import gTTS
import pygame
import threading
import os

class HtkAudioPlayer(Subject):
    def __init__(self):
        self._observers = []
        self.gtts = None
        self.rec = sr.Recognizer()
        self.logger = HtkApplicationLogger()
        self.logger.log("HtkAudioPlayer initialized.")
        self.thread = None

    def initRecon(self):
        self.logger.log("Microphone initialized for audio recognition.")
        while True:
            with sr.Microphone() as FONT:
                self.rec.adjust_for_ambient_noise(FONT)  # Ajuste para ruído ambiente (consigo melhorar isso?)
                input_audio = self.rec.listen(FONT)
                try:
                    output_in_text = self.rec.recognize_google(input_audio, language="pt-BR")
                    self.output_text = output_in_text
                    self.enableOutputAudio(output_in_text)
                    print("HTK Assistant AI YOU SAY:", output_in_text)
                    self.logger.log(f"Audio recognized: {output_in_text}")
                    
                    
                    self.notify_observers({'recon_output_in_text': output_in_text})
                    
                except sr.UnknownValueError:
                    print("HTK Assistant AI - could not understand audio.")
                    self.logger.log("Audio recognition failed: UnknownValueError - could not understand audio.")
                except sr.RequestError:
                    print("HTK Assistant AI - service connection error.")
                    self.logger.log("Audio recognition failed: RequestError - service connection error.")
            
    def initializeRecon(self):
        self.thread = threading.Thread(target=self.initRecon)
        self.thread.start()
    
    def stopRecon(self):
        if self.thread and self.thread.is_alive():
            # Note: There's no direct way to stop the thread safely in Python.
            # You would need to implement a flag to signal the thread to exit gracefully.
            self.logger.log("Stopping audio recognition thread is not implemented.")
            print("Stopping audio recognition thread is not implemented.")
            
    def enableOutputAudio(self, text):
        # Implement text-to-speech functionality here if needed
        path_output_audio = HtkOsEnvironment.get_absolute_path() + "\\audio\output.mp3"
        self.gtts = gTTS(text=text, lang='PT-BR')
        self.gtts.save(path_output_audio)
        self.logger.log(f"Audio output generated and saved to {path_output_audio}.")
        q = os.path.join(HtkOsEnvironment.get_absolute_path(), "audio", "output.mp3")
      
        pygame.mixer.init()
        pygame.mixer.music.load(q)
        pygame.mixer.music.play()
        
        # Espera terminar
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
            
        # Libera o arquivo
        pygame.mixer.music.stop()
        pygame.mixer.quit()
        
    
    def disableOutputAudio(self):
        pass
        
            