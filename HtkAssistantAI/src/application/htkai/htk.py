from core.setup.config_environment import initialize_environment
from core.extensions.prompt_fliget_appearence import setup_terminal_appearance
from core.setup.config_environment import environments_config
from core.LLMs.model.roles import RoleType
from application.ui.utils import show_toast
from core.utils.design.observer.observer import ClientObserver as OptionsObserver
from core.LLMs.htk_llm_factory import setupHtkAssistantModel
from application.ui.main_frame import MainFrame

def main():
    """Main function to initialize the HtkAssistantAI application.
    This function sets up the terminal appearance, initializes the environment configuration,
    and starts the main application frame.  """
    setup_application()
    initialize_main_frame()

def setup_application(): 
    # Load terminal appearance
    setup_terminal_appearance()

    # Initialize the environment configuration
    initialize_environment()

def initialize_main_frame():
    frame = MainFrame()
    
    options_observer = OptionsObserver(
        onSuccess=lambda response: setupHtkAssistantModel(
            response = response,callback=lambda res: frame.update_chat(res)
        ),
        onFailure=lambda _: show_toast(f"Digite algo", duration=5000))
    
    frame.register_observer(options_observer)
    
    frame.run()