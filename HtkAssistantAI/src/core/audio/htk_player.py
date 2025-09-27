import speech_recognition as sr
from core.log.htk_logger import HtkApplicationLogger
import threading

class HtkAudioPlayer:
    def __init__(self):
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
                    print("HTK Assistant AI YOU SAY:", output_in_text)
                    self.logger.log(f"Audio recognized: {output_in_text}")
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
        
            