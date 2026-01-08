import threading
import asyncio
import edge_tts
import pygame
import time
import uuid
import os

class HtkSpeaker:
    def __init__(self, logger=None):
        self.logger = logger
        if self.logger:
            self.logger.log("HtkSpeaker initialized.")

        pygame.mixer.init()
        self.lock = threading.Lock()

    async def _generate_audio(self, text, filename):
        communicate = edge_tts.Communicate(
            text,
            voice="pt-BR-AntonioNeural",
            rate="+20%",
            volume="+100%"
        )
        await communicate.save(filename)

    def _worker(self, text, onMixerBusy):
        with self.lock:
            if onMixerBusy:
                onMixerBusy(True)

            filename = f"tts_{uuid.uuid4().hex}.mp3"

            asyncio.run(self._generate_audio(text, filename))

            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(0.05)

            pygame.mixer.music.unload()  
            os.remove(filename)         

            if onMixerBusy:
                onMixerBusy(False)

    def play_audio(self, text, onMixerBusy=None):
        threading.Thread(
            target=self._worker,
            args=(text, onMixerBusy),
            daemon=True
        ).start()