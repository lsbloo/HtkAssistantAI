from core.LLMs.base.htk_base import HtkLLMOptionsBase

class SonnetOptions(HtkLLMOptionsBase):
    def __init__(self):
        super().__init__(
            chat=True, chat_with_roles=True, response=False, image_generation=False
        )

def sonnet_options():
    return SonnetOptions()

def input_sonnet_options():
    return SonnetOptions().get_input_options()
