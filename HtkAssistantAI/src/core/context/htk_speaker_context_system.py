from core.audio.htk_speaker import HtkSpeaker
from core.log.htk_logger import HtkApplicationLogger
from core.context.htk_loader_context import HtkLoaderContext

class HtkSpeakerContextSystem:
    def __init__(self):
        self._logger = HtkApplicationLogger()
        self._speaker = HtkSpeaker(logger=self._logger)
        self._htk_context = HtkLoaderContext()

    def initialize_system_audio_context(self, key):
        self._logger.log("Initializing Speaker System Audio Context...")
        output = self._htk_context.load_context_system_audio(key)
        self._speaker.play_audio(
            output,
            onMixerBusy=lambda busy: self._logger.log(
                f"Speaker System Audio Context - Mixer Busy: {busy}"
            ),
        )

    def speak_response_system(self, message):
        self._speaker.play_audio(
            message,
            onMixerBusy=lambda busy: self._logger.log(
                f"Speaker System Audio Context - Mixer Busy: {busy}"
            ),
        )


class HtkSpeakerContextSystemInitializer:
    _instance = None
    _instance_groq = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def getInstance(self):
        return HtkSpeakerContextSystem()
