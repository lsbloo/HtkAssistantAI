from core.LLMs.base.htk_base import HtkLLMOptionsBase

class GroqOptions(HtkLLMOptionsBase):
    def __init__(self):
        super().__init__(
            chat=True, chat_with_roles=True, response=False, image_generation=False
        )
        
        self.client_config_options = [
            "model_name",
            "temperature",
            "max_tokens",
            "max_retries",
            "n",
        ]
        self.client_config_options_default = {
                "model_name": "llama-3.3-70b-versatile",
                "temperature": 0.7,
                "max_tokens": 1000,
                "max_retries": 3,
                "n" : 1,
            }
    
    def get_client_config_options(self):
        return self.client_config_options
    
    def get_client_config_options_default(self):
        return self.client_config_options_default
    
def groq_options():
    return GroqOptions()

def input_groq_options():
    return GroqOptions().get_input_options()
