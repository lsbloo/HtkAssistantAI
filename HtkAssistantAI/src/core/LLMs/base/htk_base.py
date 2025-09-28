

# not yet implemented
class HtkClientBase(object):
    pass


class HtkLLMOptionsBase(object):
    def __init__(self, chat, chat_with_roles, response, image_generation):
        self.input_options = {
            "simple_chat": chat,
            "chat_with_roles": chat_with_roles,
            "response": response,
            "image_generation": image_generation
        }
    def get_input_options(self):
        return self.input_options
