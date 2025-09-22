

"""
Observer Design Pattern Implementation.
its used to allow a subject (MainFrame) to notify multiple observers (e.g., clients) about state changes.
"""
class ClientObserver:
    
    def __init__(self, model):
        self.model = model
    
    
    def update(self, data):
        data = data
        """Handle the notification from the MainFrame."""
        print(f'Observer received data: {data}')
        
        if not data['user_input']:
            print("No user input provided.")
            return
        
        if data['selected_model'] == 'Groq':
            response = self.model.chat_with_roles(message=data['user_input'], role='user')
            print(f"Response from Groq model: {response}")
        
        
        



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