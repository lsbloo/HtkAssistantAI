
from core.log.htk_logger import HtkApplicationLogger
from core.concurrency.htk_threads_manager import htkThreadsManager
"""
Observer Design Pattern Implementation.
its used to allow a subject (MainFrame) to notify multiple observers (e.g., clients) about state changes.
"""
class ClientObserver:
    
    def __init__(self, onSuccess = None, onFailure = None):
        self.onSuccess = onSuccess
        self.onFailure = onFailure
        self.logger = HtkApplicationLogger()
    
    def update(self, data):
        data = data
        """Handle the notification from the MainFrame."""
        self.logger.log(f'Observer received data: {data}')
        if self._checkKeys(data) == False:
            self.onFailure("No user input provided.")
            self.logger.log("No user input provided.")
            return
    
        def worker():
            try:
                if self.onSuccess:
                    # roda setupHtkAssistantModel em thread separada
                    self.onSuccess(data)
            except Exception as e:
                if self.onFailure:
                    self.onFailure(str(e))
        
        
        # Creating a new thread from execute LLM and not interferes in UI main frame
        htkThreadsManager().createThreadAndInitialize("Observable - LLM Rule", target=worker)
    
    def _checkKeys(self, data: dict) -> bool:
        return len(data) > 0
    

class Subject:
    def register_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def unregister_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, data):
        for observer in self._observers:
            observer.update(data)