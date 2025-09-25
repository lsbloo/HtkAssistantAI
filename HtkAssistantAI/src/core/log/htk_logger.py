import logging
import datetime
from core.utils.os_env.os_env import HtkOsEnvironment


class HtkApplicationLogger:
    def __init__(self):
        self.isDebug = HtkOsEnvironment.isDebugEnvinronmentWithLogEnabled()
        self.logPath = HtkOsEnvironment.getFileLogPath()
        self.logger = logging.getLogger(__name__)
        
        logging.basicConfig(filename= self.logPath, encoding='utf-8', level=logging.DEBUG if self.isDebug else logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger.setLevel(logging.DEBUG if self.isDebug else logging.INFO)
    
    
    def log(self, message):
        if (self.isDebug): 
            self.logger.debug(message) 
            print("",datetime.datetime.now().strftime("%A %D %B %y %I:%M"), "--",f"DEBUG: {message}")
        else: 
            self.logger.info(message)
            print("",datetime.datetime.now().strftime("%A %D %B %y %I:%M"), "--",f"INFO: {message}")
    