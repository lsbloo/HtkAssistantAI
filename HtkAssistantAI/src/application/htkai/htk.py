from core.setup.config_environment import initialize_environment
from core.extensions.prompt_fliget_appearence import setup_terminal_appearance
from core.setup.config_environment import environments_config
from core.LLMs.model.roles import RoleType
from application.ui.utils import show_toast
from core.utils.design.observer.observer import ClientObserver
from core.LLMs.htk_llm_factory import setupHtkAssistantModel
from application.ui.main_frame import MainFrame


def main():
    """Main function to initialize the HtkAssistantAI application.
    This function sets up the terminal appearance, initializes the environment configuration,
    and starts the main application frame.  """
    
    # Load terminal appearance
    setup_terminal_appearance()

    # Initialize the environment configuration
    initialize_environment()
    
    frame = MainFrame()
    
    
    client_observer = ClientObserver(
        onSuccess=lambda response: setupHtkAssistantModel(
            response = response,callback=lambda res: frame.update_chat(res)
        ),
        onFailure=lambda _: show_toast(f"Digite algo", duration=5000))
    
   
    print("Registering observer...")
    
    frame.register_observer(client_observer)
    
    
    frame.run()
    
    

    
    