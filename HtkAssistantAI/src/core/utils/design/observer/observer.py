

"""
Observer Design Pattern Implementation.
its used to allow a subject (MainFrame) to notify multiple observers (e.g., clients) about state changes.
"""
class ClientObserver:
    
    def __init__(self, callback = None):
        self.callback = callback
    
    def update(self, data):
        data = data
        """Handle the notification from the MainFrame."""
        print(f'Observer received data: {data}')
        
        if not data['user_input']:
            print("No user input provided.")
            return
        
        self.callback(data)
            

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