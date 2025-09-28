
import threading
import time
from core.log.htk_logger import HtkApplicationLogger

class HtkThreadManager:
    
    # Singleton Class
    _instance = {}
    
    def __call__(cls,*args,**kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]    
        
    def __init__(self):
        self._logger = HtkApplicationLogger()
        self._pool = []
        self._logger.log("Initializing Thread Manager")
    
    def createThreadAndInitialize(self, threadName: str, target):
        thread = HtkThreadWrapper(target=target)
        self._pool.append(HtkThread(name = threadName, thread=thread))
        d = "Creating and initializing thread ->" + threadName
        self._logger.log(d)
        thread.start()
        
    def stopAllThreads(self):
        for htkThread in self._pool:
            htkThread.thread.stop()

    def stopThread(self, threadName: str):
        for htkThread in self._pool:
            if threadName == htkThread.name:
                d = "Stopping thread -> " + threadName
                self._logger.log(d)
                htkThread.thread.stop()
        
class HtkThreadWrapper(threading.Thread):
    def __init__(self,target):
        super(HtkThreadWrapper, self).__init__(target=target)
        self.kill = threading.Event()
        self._logger = HtkApplicationLogger()

    def run(self):
        while not self.kill.is_set():
            self._logger.log("Thread executando ->")
            time.sleep(1)

    def stop(self):
        self._logger.log("Thread parando ->")
        self.kill.set()
        
class HtkThread:
    def __init__(self, name: str, thread: HtkThreadWrapper):
        self.name = name
        self.thread = thread


def htkThreadsManager():
    return HtkThreadManager()