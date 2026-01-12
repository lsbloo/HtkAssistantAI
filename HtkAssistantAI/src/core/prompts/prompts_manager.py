from core.database.htk_model_config_dao import HtkModelConfigDAO
from core.models.models_config import ModelConfig


## Setup Prompt Parameters in base class models
class HtkPromptsModelInitializerManager:
    def __init__(self):
        self._dao = HtkModelConfigDAO()

    def find_model_config_by_name(self, model) -> ModelConfig:
        return self._dao.find_model_config_by_name(model=model)

    def save_model_config_by_name(self, model, params) -> bool:
        model = ModelConfig(
            name=model,
            model_name=params.get("model_name"),
            temperature=params.get("temperature"),
            max_token=params.get("max_tokens"),
            max_retries=params.get("max_retries"),
            n=params.get("n")
        )
        try:
            self._dao.insert_table_model_config(model)
        except:
            return False
        return True
