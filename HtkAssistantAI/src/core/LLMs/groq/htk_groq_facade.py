from core.log.htk_logger import HtkApplicationLogger

class GroqClientFacade():
    def __init__(self, driver):
        self.client = driver # Instance of HtkGroqClient
        self.logger = HtkApplicationLogger()

    def chat_with_roles(self, message, role):
        self.logger.log(f"GroqClientFacade: chat_with_roles called with role: {role}")
        return self.client.chat_with_roles(message=message, role=role)
    
    def chat(self, message):
        self.logger.log("GroqClientFacade: chat called")
        return self.client.chat(message=message)