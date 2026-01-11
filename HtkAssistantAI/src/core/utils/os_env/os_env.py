import os
from core.setup.config_environment import environments_config


class HtkOsEnvironment:

    @staticmethod
    def list_directory_contents(path):
        try:
            return os.listdir(path)
        except FileNotFoundError:
            return []

    @staticmethod
    def get_absolute_path_for_resource_page_html(resource_file):
        if resource_file is None or resource_file == "":
            return os.path.abspath("").replace("src", "res\\html_pages\\")

        script_directory = os.path.abspath("").replace("src", "res\\html_pages\\")
        path = os.path.join(script_directory, resource_file)
        return path

    @staticmethod
    def get_absolute_path_for_resource_context_system(resource_file):
        if resource_file is None or resource_file == "":
            return os.path.abspath("").replace("src", "res\\context\\audio\\")

        script_directory = os.path.abspath("").replace("src", "res\\context\\audio\\")
        path = os.path.join(script_directory, resource_file)
        return path

    @staticmethod
    def get_absolute_path_for_resource_context_personas(resource_file):
        if resource_file is None or resource_file == "":
            return os.path.abspath("").replace("src", "res\\context\\other\\personas\\")

        script_directory = os.path.abspath("").replace(
            "src", "res\\context\\other\\personas\\"
        )
        path = os.path.join(script_directory, resource_file)
        return path

    @staticmethod
    def get_absolute_path_for_resource(resource_file="no-face.ico"):
        script_directory = os.path.abspath("").replace("src", "res")
        path = os.path.join(script_directory, resource_file)
        return path

    @staticmethod
    def get_absolute_path():
        script_directory = os.path.abspath("").replace("src", "res")
        path = os.path.join(script_directory)
        return path

    @staticmethod
    def getModelsAvailableInEnvironment():
        available_models = []
        required_keys = {
            "HTK_ASSISTANT_API_KEY_LLM_ANTHROPIC": "",
            "HTK_ASSISTANT_API_KEY_LLM_GROQ": "",
            "HTK_ASSISTANT_API_KEY_LLM_CHATGPT": "",
            "HTK_ASSISTANT_API_KEY_LLM_GEMINI": "",
        }
        for key, _ in required_keys.items():
            if environments_config.get(key) != None:
                available_models.append(key)
        return available_models

    @staticmethod
    def getImageProfileInEnvironment():
        image_path = environments_config.get(
            "HTK_ASSISTANT_PROFILE_IMAGE_PATH", "application/ui/assets/htk_profile.png"
        )
        return image_path

    @staticmethod
    def isDebugEnvinronmentWithLogEnabled():
        return (
            environments_config.get("HTK_ASSISTANT_DEBUG", "False") == "True"
            and environments_config.get("HTK_ASSISTANT_LOG_LEVEL", "INFO") == "DEBUG"
        )

    @staticmethod
    def getFileLogPath():
        return environments_config.get("HTK_ASSISTANT_LOG_FILE_PATH", "htkinfos.log")
