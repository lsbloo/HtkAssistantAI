
import os
from core.setup.config_environment import environments_config

class HtkOsEnvironment:
    @staticmethod
    def get_absolute_path_for_resource(resource_file="no-face.ico"):
        script_directory = os.path.abspath("").replace("src", "res")
        path = os.path.join(script_directory, resource_file)
        return path

    @staticmethod
    def getModelsAvailableInEnvironment():
        available_models = []
        required_keys = {
                'HTK_ASSISTANT_API_KEY_LLM_GROQ': "",
                'HTK_ASSISTANT_API_KEY_LLM_CHATGPT': "",
                'HTK_ASSISTANT_API_KEY_LLM_GEMINI': "",
            }
        for key, _ in required_keys.items():
            if environments_config.get(key) != None:
                available_models.append(key)
        return available_models

    @staticmethod
    def getImageProfileInEnvironment():
        image_path = environments_config.get('HTK_ASSISTANT_PROFILE_IMAGE_PATH', 'application/ui/assets/htk_profile.png')
        return image_path
    
    @staticmethod
    def isDebugEnvinronmentWithLogEnabled():
        return environments_config.get('HTK_ASSISTANT_DEBUG', 'False') == 'True' and environments_config.get('HTK_ASSISTANT_LOG_LEVEL', 'INFO') == 'DEBUG'