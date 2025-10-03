import pyttsx3

class HtkSpeaker:
    def __init__(self, logger=None):
        self.logger = logger
        self.logger.log("HtkSpeaker initialized.")

    def _speak(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 250) # velocidade do audio
        engine.setProperty('volume', 1) # volume 0 = 0% a 1 = 100%
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        del engine         
    def play_audio(self, text):
        self._speak(text=text)       