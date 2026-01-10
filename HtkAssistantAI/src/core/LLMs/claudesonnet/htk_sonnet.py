
from ..base.htk_base import HtkClientBase
from core.setup.config_environment import environments_config
from anthropic import Anthropic

SONNET_CLIENT_DEFAULT_ROLE = "user"
SONNET_CLIENT_DEFAULT_MODEL = "claude-sonnet-4-5-20250929"

class HtkSonnetClient(HtkClientBase):
    def __init__(self, api_key=None):
        api_key = api_key
        if not api_key:
            raise ValueError("API key for Claude Sonnet is not set in the environment configuration.")

        self.client = Anthropic(api_key=api_key)

    def chat(self, message, additionalContext=None) -> str:
        message = self.client.messages.create(
            max_tokens=1024,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"content": message}
            ],
            model = SONNET_CLIENT_DEFAULT_MODEL,
        )
        return message.content


class HtkSonnetInitializer:
    _instance = None
    _instance_groq = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def getInstanceSonnet(self): 
        if self._instance_groq is None:
            self._instance_groq = HtkSonnetClient(environments_config.get('HTK_ASSISTANT_API_KEY_LLM_ANTHROPIC'))
        return self._instance_groq
    