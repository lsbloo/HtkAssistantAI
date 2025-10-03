from core.LLMs.groq.htk_groq import HtkGroqInitializer
from core.LLMs.groq.htk_groq_facade import GroqClientFacade
from core.LLMs.model.roles import RoleType
from core.setup.config_environment import environments_config


def setupHtkAssistantModel(response, callback=None):
    if response['selected_model'] == 'Groq':
        groq = GroqClientFacade(driver = HtkGroqInitializer().getInstanceGroq())
        option = response['selected_option']
        if option == 'simple_chat':
            if response['is_recon_enabled'] == True:
                response = groq.chat(message=response['input_from_recon'])
                callback({"response": response, "is_recon_enabled": True})
            else:
                response = groq.chat(message=response['user_input'])
                callback({"response": response, "is_recon_enabled": False})
        elif option == 'chat_with_roles':
            if response['is_recon_enabled'] == True:
                response = groq.chat_with_roles(message=response['input_from_recon'], role=RoleType.fromType(response['option_role_choice']))
                callback({"response": response, "is_recon_enabled": True})
            else:
                response = groq.chat_with_roles(message=response['user_input'], role=RoleType.fromType(response['option_role_choice']))
                callback({"response": response, "is_recon_enabled": False})
            
        
    else:
        return None