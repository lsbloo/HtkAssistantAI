import speech_recognition as sr
from core.log.htk_logger import HtkApplicationLogger
from core.utils.design.observer.observer import Subject
from core.utils.os_env.os_env import HtkOsEnvironment
from core.audio.htk_mixer import HtkAudioMixer
from gtts import gTTS
import threading
import os

class HtkAudioPlayer(Subject):
    def __init__(self):
        self._observers = []
        self._gtts = None
        self._rec = sr.Recognizer()
        self._logger = HtkApplicationLogger()
        self._mixer = HtkAudioMixer(logger=self._logger)
        self._logger.log("HtkAudioPlayer initialized.")
        self._thread = None
        self._isEnabledOutputAudio = True # Flag to control audio output
        

    def initRecon(self):
        self._logger.log("Microphone initialized for audio recognition.")
        while True:
            with sr.Microphone() as FONT:
                self._rec.adjust_for_ambient_noise(FONT)  # Ajuste para ruído ambiente (consigo melhorar isso?)
                input_audio = self._rec.listen(FONT)
                try:
                    output_in_text = self._rec.recognize_google(input_audio, language="pt-BR")
                    self.output_text = output_in_text
                    
                    if self._isEnabledOutputAudio:
                        self.enableOutputAudio(output_in_text)
                    else:
                        self.disableOutputAudio()
                    
                    print("HTK Assistant AI YOU SAY:", output_in_text)
                    self.logger.log(f"Audio recognized: {output_in_text}")
                    
                    
                    self.notify_observers({'recon_output_in_text': output_in_text})
                    
                except sr.UnknownValueError:
                    print("HTK Assistant AI - could not understand audio.")
                    self._logger.log("Audio recognition failed: UnknownValueError - could not understand audio.")
                except sr.RequestError:
                    print("HTK Assistant AI - service connection error.")
                    self._logger.log("Audio recognition failed: RequestError - service connection error.")
            
    def initializeRecon(self):
        self._thread = threading.Thread(target=self.initRecon)
        self._thread.start()
    
    def stopRecon(self):
        if self._thread and self._thread.is_alive():
            # Note: There's no direct way to stop the thread safely in Python.
            # You would need to implement a flag to signal the thread to exit gracefully.
            self._logger.log("Stopping audio recognition thread is not implemented.")
            print("Stopping audio recognition thread is not implemented.")
            
    def enableOutputAudio(self, text):
        # Implement text-to-speech functionality here if needed
        path_output_audio = HtkOsEnvironment.get_absolute_path() + "\\audio\output.mp3"
        self._gtts = gTTS(text=text, lang='PT-BR')
        self._gtts.save(path_output_audio)
        self._logger.log(f"Audio output generated and saved to {path_output_audio}.")
        self._mixer.play_audio(os.path.join(HtkOsEnvironment.get_absolute_path(), "audio", "output.mp3"))
      
    def disableOutputAudio(self):
        self._mixer.stop_audio()
        self._isEnabledOutputAudio = False
        
    def isEnabledOutputAudio(self, isEnabled: bool):
        self._isEnabledOutputAudio = isEnabled