
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
    