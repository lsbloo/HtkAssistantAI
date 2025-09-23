import logging
from core.extensions.enviroments import isDebugEnvinronmentWithLogEnabled


class HtkApplicationLogger:
    def __init__(self):
        self.isDebug = isDebugEnvinronmentWithLogEnabled()
    
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename='htkinfos.log', encoding='utf-8', level=logging.DEBUG if self.isDebug else logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger.setLevel(logging.DEBUG if self.isDebug else logging.INFO)
    
    
    def log(self, message):
        if (self.isDebug): 
            self.logger.debug(message) 
            print(f"DEBUG: {message}")
        else: 
            self.logger.info(message)
            print(f"INFO: {message}")
    