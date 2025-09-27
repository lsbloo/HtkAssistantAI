import speech_recognition as sr
from core.log.htk_logger import HtkApplicationLogger
import threading

class HtkAudioPlayer:
    def __init__(self):
        self.rec = sr.Recognizer()
        self.logger = HtkApplicationLogger()
        self.logger.log("HtkAudioPlayer initialized.")

    def initRecon(self):
        while True:
            with sr.Microphone() as fonte:
                self.logger.log("Microphone initialized for audio recognition.")
                self.rec.adjust_for_ambient_noise(fonte)  # Ajuste para ruído ambiente
                audio = self.rec.listen(fonte)

                try:
                    texto = self.rec.recognize_google(audio, language="pt-BR")
                    print("Você disse:", texto)
                except sr.UnknownValueError:
                    print("Não consegui entender o que foi dito.")
                except sr.RequestError:
                    print("Erro ao se conectar ao serviço de reconhecimento.")
            
    def initializeRecon(self):
        thread = threading.Thread(target=self.initRecon)
        thread.start()
        
            