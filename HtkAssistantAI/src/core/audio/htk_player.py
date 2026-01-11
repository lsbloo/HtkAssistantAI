import speech_recognition as sr
from threading import Thread, Event
from core.log.htk_logger import HtkApplicationLogger
from core.utils.design.observer.observer import Subject
from core.audio.htk_speaker import HtkSpeaker

class HtkAudioPlayer(Subject):
    def __init__(self):
        self._observers = []
        self._rec = sr.Recognizer()
        self._logger = HtkApplicationLogger()
        self._mixer = HtkSpeaker(logger=self._logger)

        self._enableOrDisableMic = False
        self._stop_recon_event = Event()
        self._thread = None

        self._logger.log("HtkAudioPlayer initialized.")

    # =========================
    # THREAD LOOP
    # =========================
    def initRecon(self):
        self._logger.log("Microphone initialized for audio recognition.")

        try:
            with sr.Microphone() as mic:
                self._logger.log("Microphone connected.")

                # Ajusta ruído UMA vez
                self._rec.adjust_for_ambient_noise(mic, duration=1)

                while not self._stop_recon_event.is_set() and self._enableOrDisableMic:
                    try:
                        audio = self._rec.listen(
                            mic,
                            timeout=1,
                            phrase_time_limit=5
                        )

                        text = self._rec.recognize_google(
                            audio,
                            language="pt-BR"
                        )

                        self.output_text = text
                        print("HTK Assistant AI YOU SAY:", text)

                        self._logger.log(f"Audio recognized: {text}")
                        self.notify_observers({"recon_output_in_text": text})

                    except sr.WaitTimeoutError:
                        # Silêncio → volta pro loop e checa stop
                        continue

                    except sr.UnknownValueError:
                        self._logger.log("Audio not understood.")

                    except sr.RequestError:
                        self._logger.log("Speech recognition service error.")

        finally:
            self._logger.log("Recognition thread finalized.")

    # =========================
    # PUBLIC API
    # =========================
    def initializeRecon(self):
        self._stop_recon_event.clear()
        self._enableOrDisableMic = True

        if self._thread and self._thread.is_alive():
            self._logger.log("Recon thread already running.")
            return

        self._thread = Thread(
            target=self.initRecon,
            daemon=True
        )
        self._thread.start()

        self._logger.log("Recon thread started.")

    def stopRecon(self):
        self._logger.log("Stopping recon thread...")
        self._enableOrDisableMic = False
        self._stop_recon_event.set()

    def enableOutputAudio(self, text, onMixerBusy=None):
        self._mixer.play_audio(text, onMixerBusy)