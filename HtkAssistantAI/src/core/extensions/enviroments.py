
from core.setup.config_environment import environments_config

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

def getImageProfileInEnvironment():
    image_path = environments_config.get('HTK_ASSISTANT_PROFILE_IMAGE_PATH', 'application/ui/assets/htk_profile.png')
    return image_path
    
def isDebugEnvinronmentWithLogEnabled():
    return environments_config.get('HTK_ASSISTANT_DEBUG', 'False') == 'True' and environments_config.get('HTK_ASSISTANT_LOG_LEVEL', 'INFO') == 'DEBUG'