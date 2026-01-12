
import customtkinter as ctk
from core.utils.design.observer.observer import Subject
from core.utils.os_env.os_env import HtkOsEnvironment
from core.prompts.setup_prompts_model import HtkPromptsModelConfiguration
from core.context.htk_speaker_context_system import HtkSpeakerContextSystemInitializer
from core.log.htk_logger import HtkApplicationLogger
from threading import Thread

class PromptConfigFrame(Subject):
    def __init__(self, app_root, isSpeakSystem ,title="HTK Assistant AI - Prompt Config"):
        self._root = app_root
        self._isSpeakSystem = isSpeakSystem
        self._systemSpeaker = HtkSpeakerContextSystemInitializer().getInstance()
        self._app = ctk.CTkToplevel(self._root)
        self._app.title(title)
        self._app.geometry("800x750")
        self._app.resizable(False, False)
        self._logger = HtkApplicationLogger()
        self._logger.log("Initializing Prompt Configuration Frame")
        self._htk_prompts_model_configuration = HtkPromptsModelConfiguration()
        self._setup_header_view()
        self._setup_models_view()
        
        self._speakSystem(key="welcome_prompt_config")
    
    def _speakSystem(self, key):
        if self._isSpeakSystem == True:
            thread = Thread(
                target=self._systemSpeaker.initialize_system_audio_context, args=(key,)
            )
            thread.start()
            
    def _setup_header_view(self):
        self._title = ctk.CTkLabel(self._app, text="Configurações de Prompt", bg_color="transparent",
            fg_color="transparent",
            font=("Arial", 18),
            height=15,
            text_color="white",)
        self._title.place(x=300,y=20)
        
    
    def _setup_models_view(self):
        self._tabview = ctk.CTkTabview(master=self._app, height=300, width=750)
        self._tabview.place(x=10, y=50)
        

        available_models = self._setupModelsBasedInEnvironment()
        
        for model in available_models:
            self._setup_view_options_for_model(model)
        
     
    def _setup_view_options_for_model(self, model: str):
        options = self._htk_prompts_model_configuration.get_client_config_options(model)
        
        tab = self._tabview.add(model)
        row = 0
        if options is None:
            self._logger.log(f"PromptConfigFrame: No options found for the model: {model}")
            label = ctk.CTkLabel(master=tab, text="No options available for this model.")
            label.grid(row=row, column=0, padx=10, pady=10, sticky="w")
            return
        else:
            self._logger.log(f"PromptConfigFrame: Setting up options for the model: {model}")
            for option in options:
                default_value = option
                label = ctk.CTkLabel(master=tab, text=f"{option}:")
                label.grid(row=row, column=0, padx=10, pady=10, sticky="w")
                    
                entry = ctk.CTkEntry(master=tab)
                entry.insert(0, str(default_value))
                entry.grid(row=row, column=1, padx=10, pady=10, sticky="w")
                    
                row += 1
                    
        
    def _setupModelsBasedInEnvironment(self):
        model_mapping = {
            "HTK_ASSISTANT_API_KEY_LLM_GROQ": "Groq",
            "HTK_ASSISTANT_API_KEY_LLM_ANTHROPIC": "Claude Sonnet",
            "HTK_ASSISTANT_API_KEY_LLM_CHATGPT": "ChatGPT",
            "HTK_ASSISTANT_API_KEY_LLM_GEMINI": "Gemini",
        }

        available_env_models = HtkOsEnvironment.getModelsAvailableInEnvironment()

        if not available_env_models:
            return ["No models available"]

        available_models = [
            model_mapping[env_model]
            for env_model in available_env_models
            if env_model in model_mapping
        ]

        return available_models if available_models else ["No models available"]
    
    def destroy(self):
        self._app.destroy()