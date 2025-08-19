
from groq import Groq
from ..setup.config_environment import environments_config

class HtkGroqClient:
    def __init__(self):
        api_key = environments_config.get('HTK_ASSISTANT_API_KEY_LLM_GROQ')
        if not api_key:
            raise ValueError("API key for Groq is not set in the environment configuration.")
        self.client = Groq(api_key=api_key)

    def generate_text(self, prompt, max_tokens=100):
        response = self.client.completions.create(
            model="groq-1",
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    
    def chat(self, messages, max_tokens=100):
        response = self.client.chat.completions.create(
            model="groq-1",
            messages=messages,
            max_tokens=max_tokens
        )
        return response.choices[0].message['content'].strip()
    
    def initialize_with_roles(self, system_message, user_message, max_tokens=100):
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message}
        ]
        return self.chat(messages, max_tokens=max_tokens)