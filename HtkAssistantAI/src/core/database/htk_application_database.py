import sqlite3
from threading import Thread, Lock
from core.log.htk_logger import HtkApplicationLogger
from core.context.htk_speaker_context_system import HtkSpeakerContextSystemInitializer

class HtkApplicationDatabase:
    _instance = None
    _connection = None
    _lock = Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if hasattr(self, "_initialized") and self._initialized:
            return

        self._initialized = True
        self._logger = HtkApplicationLogger()
        self._systemSpeaker = HtkSpeakerContextSystemInitializer().getInstance()
        self._isSpeakSystem = True

        try:
            HtkApplicationDatabase._connection = sqlite3.connect("storage/htk_database.db", check_same_thread=False)
        except Exception as e:
            self._logger.log(f"Failure to connect local database: {e}")
            self._speakSystem("database_failure_connection")

    def _speakSystem(self, key):
        if self._isSpeakSystem:
            thread = Thread(
                target=self._systemSpeaker.initialize_system_audio_context,
                args=(key,)
            )
            thread.start()

    @staticmethod
    def getConnection():
        if HtkApplicationDatabase._instance is None:
            HtkApplicationDatabase()
        return HtkApplicationDatabase._connection