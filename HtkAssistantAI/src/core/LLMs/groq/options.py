from core.LLMs.base.htk_base import HtkLLMOptionsBase
from core.prompts.prompts_manager import HtkPromptsModelInitializerManager

class GroqOptions(HtkLLMOptionsBase):
    def __init__(self):
        super().__init__(
            chat=True, chat_with_roles=True, response=False, image_generation=False
        )
        self._prompt_manager = HtkPromptsModelInitializerManager()
        default_model_config = self._prompt_manager.find_model_config_by_name("Groq")
        
        self.client_config_options = {
            "model_name": "O tipo de modelo que você deseja utilizar. \n (default = llama-3.3-70b-versatile)",
            "temperature": "Define o nível de criatividade nas respostas do modelo, (valor flutuante entre 0 a 1). \n (default 0.7)",
            "max_tokens": "Número máximo de tokens de entrada (inputs) desejados. \n (default = 1000)",
            "max_retries": "Número de re-tentativas que o modelo refaz para obter a melhor resposta. \n (default = 1)",
            "n": "Número de repostas completas para cada prompt. \n (default = 1)"
        }
        self.client_config_options_default = {
                "model_name": default_model_config.model_name,
                "temperature": default_model_config.temperature,
                "max_tokens": default_model_config.max_token,
                "max_retries": default_model_config.max_retries,
                "n" : default_model_config.n,
            }
        
        self.client_config_general_options = {
            "Exemplos de model_name": ["llama-3.3-70b-versatile", "mixtral-8x7b-32768"]
        }
    
    def get_client_config_options(self):
        return self.client_config_options
    
    def get_client_config_options_default(self):
        return self.client_config_options_default
    
    def get_client_config_general_options_default(self):
        return self.client_config_general_options
    
def groq_options():
    return GroqOptions()

def input_groq_options():
    return GroqOptions().get_input_options()
