from core.log.htk_logger import HtkApplicationLogger
from core.models.models_config import ModelConfig
from .repositories.model_config_repository import ModelConfigRepository
    
class HtkModelConfigDAO():
    def __init__(self):
        self._logger = HtkApplicationLogger()
        self._repository = ModelConfigRepository()
    
    def create_table_model_config(self):
        self._logger.log("Creating new table of model configurations")
        self._repository.create_table()
        self._logger.log("New table of model configurations has created")
    
    def insert_table_model_config(self, model: ModelConfig):
        self._logger.log("Insert new data in model_config table")
        self._repository.save(model=model)
        self._logger.log("Insert new data in model_config table is successful")
    
    def find_model_config_by_name(self, model) -> ModelConfig:
        self._logger.log("Find model config by name is called")
        return self._repository.find_by_name(model)
        
    