from core.extensions.enviroments import isDebugEnvinronmentWithLogEnabled

class GroqOptions(object):
    def __init__(self):
        self.input_options = {
            "chat": True,
            "chat_with_roles": True,
            "response": True,
            "image_generation": False
        }
    
    def get_input_options(self):
        return self.input_options  



def set_input_groq_options():
    return GroqOptions().get_input_options()