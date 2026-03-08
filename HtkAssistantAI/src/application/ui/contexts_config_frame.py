import customtkinter as ctk
from core.utils.design.observer.observer import Subject
from core.utils.os_env.os_env import HtkOsEnvironment
from core.context.htk_speaker_context_system import HtkSpeakerContextSystemInitializer
from core.log.htk_logger import HtkApplicationLogger
from threading import Thread
from PIL import Image
import time

class ContextFrame(Subject):
    def __init__(
        self, app_root, isSpeakSystem, title="HTK Assistant AI - Contexts Config"
    ):
        self._root = app_root
        self._isSpeakSystem = isSpeakSystem
        self._systemSpeaker = HtkSpeakerContextSystemInitializer().getInstance()
        self._app = ctk.CTkToplevel(self._root)
        self._app.title(title)
        self._app.geometry("1100x550")
        self._app.resizable(False,False)
        self._app.configure(bg="#1E1E1E")
        self._logger = HtkApplicationLogger()
        self._logger.log("Initializing Context Configuration Frame")
        self._speakSystem(key="welcome_context_config")
        
    def _speakSystem(self, key):
        if self._isSpeakSystem == True:
            thread = Thread(
                target=self._systemSpeaker.initialize_system_audio_context, args=(key,)
            )
            thread.start()
    