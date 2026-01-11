## Handle for loading contexts from application ##
from core.log.htk_logger import HtkApplicationLogger
from core.utils.os_env.os_env import HtkOsEnvironment
import json

class HtkLoaderContext:

    def __init__(self):
        self._logger = HtkApplicationLogger()

    def load_persona_with_resource_file(self, resource_file):
        absolute_path = (
            HtkOsEnvironment.get_absolute_path_for_resource_context_personas(
                resource_file=resource_file
            )
        )
        with open(absolute_path, "r", encoding="utf-8") as file:
            json_string = file.read()
            data = json.loads(json_string)
            self._logger.log(f"Persona '{data['name']}' loaded from {absolute_path}")
            return json_string

    def load_contexts_personas_available(self):
        absolute_path = (
            HtkOsEnvironment.get_absolute_path_for_resource_context_personas(
                resource_file=None
            )
        )
        personas_available = HtkOsEnvironment.list_directory_contents(absolute_path)
        return personas_available

    def load_context_system_audio(self, key):
        absolute_path = HtkOsEnvironment.get_absolute_path_for_resource_context_system(
            resource_file="first_interaction.json"
        )
        with open(absolute_path, "r", encoding="utf-8") as file:
            json_string = file.read()
            data = json.loads(json_string)
            self._logger.log(
                f"Audio Message'{data['audio'].get(key)}' loaded from {absolute_path}"
            )
            return data["audio"].get(key)
