from core.LLMs.base.htk_base import HtkLLMOptionsBase

class GroqOptions(HtkLLMOptionsBase):
    def __init__(self):
        super().__init__(
            chat=True,
            chat_with_roles=True,
            response=False,
            image_generation=False
        )

def input_groq_options():
    return GroqOptions().get_input_options()