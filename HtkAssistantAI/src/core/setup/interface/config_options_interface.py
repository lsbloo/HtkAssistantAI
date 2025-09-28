 
 
 
 ## Dynamic onfigurations of interface based in JSON
import os
import json
from core.log.htk_logger import HtkApplicationLogger
from core.utils.design.observer.observer import Subject
 
class HtkLoaderConfigInterface(Subject):
    def __init__(self):
        self._observers = []
        self._config_file = "config_interface.json"
        self._logger = HtkApplicationLogger()
        self._logger.log("Initializing configuration interface")
    
    def _initialize(self):
        configurations = self._load_configs_interface()
        dList = []
        for key in configurations:
            dList.append(HtkLoaderConfig(name = key, propertie = configurations.get(key)))
            
        self.notify_observers(dList)
        self._logger.log("Finished loading configuration interface")
        return dList
        
    def init(self):
        self._initialize()
        
    def _load_default_configs_inteface(self):
        return {
            "Configurações": {"Ativar Recoginição": False , "Modo Escuro": False, "Ativar Som": False},
            "Documentação": {"⚡️Github⚡️": "https://github.com/lsbloo/HtkAssistantAI"}
        }
        
    def _load_configs_interface(self):
        if(os.path.exists(self._config_file)):
            with open(self._config_file, "r", encoding="UTF-8") as config:
                return json.load(config)
        else:
            return self._load_default_configs_inteface()



class HtkLoaderConfig():
    def __init__(self, name, propertie):
        self.name = name
        self.propertie = propertie