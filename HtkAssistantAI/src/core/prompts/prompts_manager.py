from core.database.htk_model_config_dao import HtkModelConfigDAO
from core.models.models_config import ModelConfig

## Setup Prompt Parameters in base class models
class HtkPromptsModelInitializerManager():
    def __init__(self):
        self._dao = HtkModelConfigDAO()
    
    def find_model_config_by_name(self, model) -> ModelConfig:
        return self._dao.find_model_config_by_name(model=model)