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
    
    """
    # Load terminal appearance
    setup_terminal_appearance()

    # Initialize the environment configuration
    initialize_environment()
    
    # Initialize Groq LLM client (example usage)
    groq_client = HtkGroqClient(environments_config.get('HTK_ASSISTANT_API_KEY_LLM_GROQ'))
    

    print("HTK Assistant AI is now running. Type 'exit' or 'quit' to stop.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Exiting the application.")
            break
        response = groq_client.chat_with_roles(
            message=user_input, role = RoleType.ASSISTANT)
        print(f"HTK Assistant AI: {response}")
    """
    
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
    
    

    
    