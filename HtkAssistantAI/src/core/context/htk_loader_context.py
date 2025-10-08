
## Handle for loading contexts from application ##
from core.log.htk_logger import HtkApplicationLogger
from core.utils.os_env.os_env import HtkOsEnvironment

class HtkLoaderContext:
    
    def __init__(self):
        self._logger = HtkApplicationLogger()
    
    def load_personas(self):
        absolute_path = HtkOsEnvironment.get_absolute_path_for_context()
        print(absolute_path)
        
        file_path = ""
        with open(file_path, "r", encoding="utf-8") as file:
            json_string = file.read()

            print("Conteúdo em string:")
            print(json_string)

            # (Opcional) Converter para objeto Python se quiser manipular
            data = json.loads(json_string)
            print("\nNome do contexto:", data["name"])
    
    def load_audio_first_interaction(self):
        # not yet
        pass
