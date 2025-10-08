import speech_recognition as sr
from core.log.htk_logger import HtkApplicationLogger
from core.utils.design.observer.observer import Subject
from core.audio.htk_speaker import HtkSpeaker
from core.concurrency.htk_threads_manager import htkThreadsManager
import threading

class HtkAudioPlayer(Subject):
    def __init__(self):
        self._observers = []
        self._gtts = None
        self._threadManager = htkThreadsManager()
        self._rec = sr.Recognizer()
        self._logger = HtkApplicationLogger()
        self._mixer = HtkSpeaker(logger=self._logger)
        self._logger.log("HtkAudioPlayer initialized.")
        self._threadName = "HtkAudioPlayer - Recongnize"
        self._isEnabledOutputAudio = False # Flag to control audio output
        self._enableOrDisableMic = False
        self._stop_recon_event = threading.Event()
        

    def initRecon(self):
        self._logger.log("Microphone initialized for audio recognition.")
        if self._enableOrDisableMic:
            with sr.Microphone() as Font:
                while not self._stop_recon_event.is_set():
                        self._rec.adjust_for_ambient_noise(Font, duration=2)  # Ajuste para ruído ambiente (consigo melhorar isso?)
                        input_audio = self._rec.listen(Font)
                        try:
                            output_in_text = self._rec.recognize_google(input_audio, language="pt-BR")
                            self.output_text = output_in_text    
                            print("HTK Assistant AI YOU SAY:", output_in_text)
                            self._logger.log(f"Audio recognized: {output_in_text}")
                            self.notify_observers({'recon_output_in_text': output_in_text})
                                
                        except sr.UnknownValueError:
                            print("HTK Assistant AI - could not understand audio.")
                            self._logger.log("Audio recognition failed: UnknownValueError - could not understand audio.")
                        except sr.RequestError:
                            print("HTK Assistant AI - service connection error.")
                            self._logger.log("Audio recognition failed: RequestError - service connection error.")
                        
            
    def initializeRecon(self):
        self._stop_recon_event.clear()
        self._enableOrDisableMic = True
        self._threadManager.createThreadAndInitialize(threadName = self._threadName, target=self.initRecon)
    
    def stopRecon(self):
        self._logger.log("Call disable recon")
        self._stop_recon_event.set()  # sinaliza para a thread parar
        self._enableOrDisableMic = False
        self._threadManager.stopThread(threadName=self._threadName)
            
    def enableOutputAudio(self, text):
        # OLD CODE 
        #unique_name = f"output_{int(time.time()*1000)}.mp3"
        #path_output_audio = HtkOsEnvironment.get_absolute_path() + "\\audio\\" + unique_name
        #self._gtts = gTTS(text=text, lang='PT-BR')
        #self._gtts.save(path_output_audio)
        #self._logger.log(f"Audio output generated and saved to {path_output_audio}.")
        self._mixer.play_audio(text)
      
    def disableOutputAudio(self):
        self._mixer.stop_audio()
        self._isEnabledOutputAudio = False
        
    def isEnabledOutputAudio(self, isEnabled: bool):
        self._isEnabledOutputAudio = isEnabled