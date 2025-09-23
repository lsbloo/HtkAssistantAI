

class GroqClientFacade():
    def __init__(self, driver):
        self.client = driver # Instance of HtkGroqClient

    def chat_with_roles(self, message, role):
        return self.client.chat_with_roles(message=message, role=role)
    
    def chat(self, message):
        return self.client.chat(message=message)