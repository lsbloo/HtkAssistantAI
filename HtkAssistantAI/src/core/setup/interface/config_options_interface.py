## Dynamic onfigurations of interface based in JSON
import os
import json
from core.log.htk_logger import HtkApplicationLogger
from core.utils.design.observer.observer import Subject
from dataclasses import dataclass
from typing import Optional, List, Dict, Any
 
class HtkLoaderConfigInterface(Subject):
    def __init__(self):
        self._observers = []
        self._config_file = "config_interface.json"
        self._logger = HtkApplicationLogger()
        self._logger.log("Initializing configuration interface")
    
    def _initialize(self):
        configurations = self._load_configs_interface()
        
        itens_config: List[Item] = []
        itens_config_link: List[Item] = []

        config = HtkConfigurationModel(
            name = "Confgurações"
        )
        config_link = HtkConfigurationModel("Documentação")
        
        # Configurações
        for key, valor in configurations.get("Configurações", {}).items():
            itens_config.append(Item(
                id=key,
                type="config",
                label=valor.get("label", ""),
                default=valor.get("default", False)
            ))

        # Documentação
        for key, valor in configurations.get("Documentação", {}).items():
            itens_config_link.append(Item(
                id=key,
                type="link",
                label=valor.get("label", ""),
                url=valor.get("url", "")
            ))
        
        config.set_items(itens_config)
        config_link.set_items(itens_config_link)
        
        print(config_link.items[0].label)
        
        self.notify_observers([config, config_link])
        self._logger.log("Finished loading configuration interface")
        
    def init(self):
        self._initialize()
        
    def _load_default_configs_inteface(self):
        return {
                "Configurações": {
                    "recon": {"label": "Ativar Recoginição", "default": False},
                    "contexto":   {"label": "Habilitar Contexto",           "default": False},
                    "som":           {"label": "Ativar Som",            "default": True},
                    "web": {"label":"Ativar Web","default": False},
                },
                "Documentação": {
                    "github": {"label": "⚡️Github⚡️", "url": "https://github.com/lsbloo/HtkAssistantAI"}
                }
            }
        
    def _load_configs_interface(self):
        if(os.path.exists(self._config_file)):
            with open(self._config_file, "r", encoding="UTF-8") as config:
                return json.load(config)
        else:
            return self._load_default_configs_inteface()


@dataclass
class Item:
    id: str
    type: str           # "config" ou "link"
    label: str
    default: Optional[bool] = None   # apenas para config
    url: Optional[str] = None  
    

class HtkConfigurationModel:
    
    def __init__(self, name):
        self.name = name
        self.items = None
    
    def set_items(self, items):
        self.items = items
    
 