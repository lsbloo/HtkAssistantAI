
from core.log.htk_logger import HtkApplicationLogger
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
        
        self.onSuccess(data)
    
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