# Setup prompts model configuration of Htk Assistant AI with available LLMs from environment variables.
from core.LLMs.groq.options import groq_options
from core.LLMs.claudesonnet.options import sonnet_options
from core.log.htk_logger import HtkApplicationLogger

class HtkPromptsModelConfiguration:
    
    def __init__(self):
        self._logger = HtkApplicationLogger()
    
    def get_client_config_options(self,model: str):
        model_mapping = {
            "Groq": groq_options(),
            "Claude Sonnet": sonnet_options(),
        }
        model_options = model_mapping.get(model, None)
        if model_options is None:
            self._logger.log(f"HtkPromptsModelConfiguration: No options found for the model: {model}")
            raise ValueError(f"No options found for the model: {model}")
        else:
            self._logger.log(f"HtkPromptsModelConfiguration: Retrieved options for the model: {model}")
            return model_options.get_client_config_options()
    
    def get_client_config_options_default(self,model: str):
        model_mapping = {
            "Groq": groq_options(),
            "Claude Sonnet": sonnet_options(),
        }
        model_options = model_mapping.get(model, None)
        if model_options is None:
            self._logger.log(f"HtkPromptsModelConfiguration: No options default found for the model: {model}")
            raise ValueError(f"No options found for the model: {model}")
        else:
            self._logger.log(f"HtkPromptsModelConfiguration: Retrieved options default for the model: {model}")
            return model_options.get_client_config_options_default()

    def get_client_config_general_options_default(self,model: str):
        model_mapping = {
            "Groq": groq_options(),
            "Claude Sonnet": sonnet_options(),
        }
        model_options = model_mapping.get(model, None)
        if model_options is None:
            self._logger.log(f"HtkPromptsModelConfiguration: No options general default found for the model: {model}")
            raise ValueError(f"No options found for the model: {model}")
        else:
            self._logger.log(f"HtkPromptsModelConfiguration: Retrieved options general default for the model: {model}")
            return model_options.get_client_config_general_options_default()