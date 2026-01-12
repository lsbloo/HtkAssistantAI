from core.database.htk_model_config_dao import HtkModelConfigDAO
from core.database.htk_model_config_dao import ModelConfig
from core.log.htk_logger import HtkApplicationLogger
from core.setup.config_environment import initialize_environment
from core.extensions.prompt_fliget_appearence import setup_terminal_appearance
from core.utils.os_env.os_env import HtkOsEnvironment

# Initialize local resource loader from database and others
class HtkResourceLoader:
    def __init__(self):
        self._logger = HtkApplicationLogger()
        self._logger.log("Resource Loader is initializing...")
        self._model_config_dao = HtkModelConfigDAO()
        
    
    def exec(self, onStartMainFrame = None):
        self._init_model_config_database()
        self._init_env(onStartMainFrame)
    
    def _init_env(self,onStartMainFrame = None):
        # Load terminal appearance
        setup_terminal_appearance()
        # Initialize the environment configuration
        initialize_environment()
        
        self._insert_model_config_default()
        onStartMainFrame()
        
    
    def _init_model_config_database(self):
        self._model_config_dao.create_table_model_config()
    
    def _insert_model_config_default(self):
        models_available = self._get_models_available()
        models_config = []
        if models_available is not None:
            for model in models_available:
                if model == "Groq":
                    models_config.append(ModelConfig(name=model,model_name="llama-3.3-70b-versatile", temperature=0.7, max_token=1000, max_retries=1, n=1))
        
        for config in models_config:
            self._model_config_dao.insert_table_model_config(config)
        
                    
    
    def _get_models_available(self):
        model_mapping = {
            "HTK_ASSISTANT_API_KEY_LLM_GROQ": "Groq",
            "HTK_ASSISTANT_API_KEY_LLM_ANTHROPIC": "Claude Sonnet",
            "HTK_ASSISTANT_API_KEY_LLM_CHATGPT": "ChatGPT",
            "HTK_ASSISTANT_API_KEY_LLM_GEMINI": "Gemini",
        }

        available_env_models = HtkOsEnvironment.getModelsAvailableInEnvironment()

        if not available_env_models:
            return ["No models available"]

        available_models = [
            model_mapping[env_model]
            for env_model in available_env_models
            if env_model in model_mapping
        ]

        return available_models if available_models else ["No models available"]
        
        