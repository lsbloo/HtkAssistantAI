class ModelConfig():
    def __init__(self, id=None, name=None, model_name=None, temperature=None, max_token=None, max_retries=None, n=None):
        self.id = id
        self.name = name
        self.model_name = model_name
        self.temperature = temperature
        self.max_token = max_token
        self.max_retries = max_retries
        self.n = n