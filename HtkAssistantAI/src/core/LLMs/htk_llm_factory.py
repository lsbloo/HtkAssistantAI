from core.LLMs.groq.htk_groq import HtkGroqClient
from core.LLMs.groq.htk_groq_facade import GroqClientFacade
from core.extensions.enviroments import environments_config

def setupHtkAssistantModel(response, callback=None):
    if response['selected_model'] == 'Groq':
        groq = GroqClientFacade(
            driver = HtkGroqClient(environments_config.get('HTK_ASSISTANT_API_KEY_LLM_GROQ'))
        )
        
        option = response['selected_option']
        if option == 'simple_chat':
            response = groq.chat(message=response['user_input'])
            callback(response)
        elif option == 'chat_with_roles':
            response = groq.chat_with_roles(message=response['user_input'], role='assistant')
            callback(response)
        
    else:
        return None
    