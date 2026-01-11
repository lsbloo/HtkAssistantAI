from core.LLMs.groq.htk_groq import HtkGroqInitializer
from core.LLMs.groq.htk_groq_facade import GroqClientFacade
from core.LLMs.claudesonnet.htk_sonnet import HtkSonnetInitializer
from core.LLMs.claudesonnet.htk_sonnet_facade import SonnetClientFacade
from core.LLMs.base.htk_base import HtkClientBase
from core.LLMs.model.roles import RoleType

def setupHtkAssistantModel(response, callback=None):
    if response["selected_model"] == "Groq":
        groq = GroqClientFacade(driver=HtkGroqInitializer().getInstanceGroq())
        execHtkAssistantModel(response, groq, callback)

    elif response["selected_model"] == "Claude Sonnet":
        sonnet = SonnetClientFacade(driver=HtkSonnetInitializer().getInstanceSonnet())
        execHtkAssistantModel(response, sonnet, callback)

def execHtkAssistantModel(response, client: HtkClientBase, callback=None):
    option = response["selected_option"]
    if option == "simple_chat":
        if response["is_recon_enabled"] == True:
            response = client.chat(
                message=response["input_from_recon"],
                additionalContext=response["option_persona_context_choice"],
            )
            callback({"response": response, "is_recon_enabled": True})
        else:
            response = client.chat(
                message=response["user_input"],
                additionalContext=response["option_persona_context_choice"],
            )
            callback({"response": response, "is_recon_enabled": False})
    elif option == "chat_with_roles":
        if response["is_recon_enabled"] == True:
            response = client.chat_with_roles(
                message=response["input_from_recon"],
                role=RoleType.fromType(response["option_role_choice"]),
                additionalContext=response["option_persona_context_choice"],
            )
            callback({"response": response, "is_recon_enabled": True})
        else:
            response = client.chat_with_roles(
                message=response["user_input"],
                role=RoleType.fromType(response["option_role_choice"]),
                additionalContext=response["option_persona_context_choice"],
            )
            callback({"response": response, "is_recon_enabled": False})
