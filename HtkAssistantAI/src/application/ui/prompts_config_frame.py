import customtkinter as ctk
from core.utils.design.observer.observer import Subject
from core.utils.os_env.os_env import HtkOsEnvironment
from core.prompts.setup_prompts_model import HtkPromptsModelConfiguration
from core.context.htk_speaker_context_system import HtkSpeakerContextSystemInitializer
from core.log.htk_logger import HtkApplicationLogger
from core.prompts.prompts_manager import HtkPromptsModelInitializerManager
from threading import Thread
from PIL import Image
import time

class PromptConfigFrame(Subject):
    def __init__(
        self, app_root, isSpeakSystem, title="HTK Assistant AI - Prompt Config"
    ):
        self._root = app_root
        self._isSpeakSystem = isSpeakSystem
        self._systemSpeaker = HtkSpeakerContextSystemInitializer().getInstance()
        self._app = ctk.CTkToplevel(self._root)
        self._app.title(title)
        self._app.geometry("1100x550")
        self._app.resizable(False,False)
        self._app.configure(bg="#1E1E1E")
        self._logger = HtkApplicationLogger()
        self._logger.log("Initializing Prompt Configuration Frame")
        self._htk_prompts_model_configuration = HtkPromptsModelConfiguration()
        self._model_entries = {}
        self._prompt_initializer_manager = HtkPromptsModelInitializerManager()
        self._setup_header_view()
        self._setup_loading_spinner()
        self._setup_models_view()
        self._speakSystem(key="welcome_prompt_config")

    def _speakSystem(self, key):
        if self._isSpeakSystem == True:
            thread = Thread(
                target=self._systemSpeaker.initialize_system_audio_context, args=(key,)
            )
            thread.start()

    def _setup_header_view(self):
        self._title = ctk.CTkLabel(
            self._app,
            text="Configurações de Prompt",
            bg_color="transparent",
            fg_color="transparent",
            font=("Arial", 18),
            height=15,
            text_color="white",
        )
        self._title.place(x=500, y=20)

    def _setup_models_view(self):
        self._tabview = ctk.CTkTabview(
            master=self._app,
            height=300,
            width=750,
            bg_color="#1E1E1E",
            corner_radius=24,
        )
        self._tabview.place(x=5, y=55)

        available_models = self._setupModelsBasedInEnvironment()

        for model in available_models:
            self._setup_view_options_for_model(model)

    def _setup_view_options_for_model(self, model: str):
        self._model_entries[model] = {}
        options = self._htk_prompts_model_configuration.get_client_config_options(model)
        default_options = (
            self._htk_prompts_model_configuration.get_client_config_options_default(
                model
            )
        )
        general_options = self._htk_prompts_model_configuration.get_client_config_general_options_default(
            model
        )
        tab = self._tabview.add(model)
        row = 0
        if options is None:
            self._logger.log(
                f"PromptConfigFrame: No options found for the model: {model}"
            )
            label = ctk.CTkLabel(
                master=tab, text="No options available for this model."
            )
            label.grid(row=row, column=0, padx=10, pady=10, sticky="w")
            return
        else:
            self._logger.log(
                f"PromptConfigFrame: Setting up options for the model: {model}"
            )
            for option in options.keys():
                label = ctk.CTkLabel(master=tab, text=f"{option}:")
                label.grid(row=row, column=0, padx=10, pady=10, sticky="w")

                entry = ctk.CTkEntry(master=tab)
                entry.insert(0, str(default_options.get(option)))
                entry.grid(row=row, column=1, padx=10, pady=10, sticky="w")
                
                self._model_entries[model][option] = entry

                label_description = ctk.CTkLabel(
                    master=tab, text=f"{options.get(option)}:"
                )
                label_description.grid(row=row, column=2, padx=10, pady=10, sticky="w")

                row += 1

            if general_options is not None:
                for general_option, items in general_options.items():
                    label_general_option = ctk.CTkLabel(
                        master=tab,
                        text=f"{general_option}:",
                        font=("Arial", 14, "bold"),
                    )
                    label_general_option.grid(
                        row=row, column=0, sticky="w", padx=10, pady=(10, 4)
                    )
                    row += 1

                    for general in items:
                        label_general = ctk.CTkLabel(master=tab, text=f"• {general}")
                        label_general.grid(
                            row=row, column=0, sticky="w", padx=25, pady=2
                        )
                        row += 1
            icon_button = ctk.CTkImage(
                light_image=Image.open(
                    HtkOsEnvironment.get_absolute_path_for_resource_icon(
                        "settings-ia-icon.png"
                    )
                ),
                dark_image=Image.open(
                    HtkOsEnvironment.get_absolute_path_for_resource_icon(
                        "settings-ia-icon.png"
                    )
                ),
                size=(20, 20),
            )

            prompts_button = ctk.CTkButton(
                    tab,
                    text="Atualizar Modelo",
                    image=icon_button,
                    compound="right",
                    command=lambda: self._update_model_with_new_params(model=model),
                    corner_radius=24,
                    fg_color="#4D0C83",
                )
            
            prompts_button.grid(row=row, column=4, sticky="se")
            row += 1
            
            
    
    def _setup_loading_spinner(self):
        self._progressbar = ctk.CTkProgressBar(
            master=self._app,
            mode="indeterminate",
            indeterminate_speed=10,
            width=1050,
            corner_radius=20,
            progress_color="#4D0C83",
        )
        self._progressbar.pack(padx=10,pady=10)
        self._progressbar.place(x=10, y=45)
        self._progressbar.stop()
        
            

    def _update_model_with_new_params(self,model):
        self._progressbar.start()
        entries = self._model_entries.get(model)
        if not entries:
            self._logger.log(f"No entries found for model {model}")
            return

        params = {}

        for option, entry in entries.items():
            value = entry.get()
            if value.isdigit():
                value = int(value)
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass

            params[option] = value

        self._logger.log(f"Updated params for {model}: {params}")
        
        self._app.after(
            2000,
            lambda model=model, params=params: self._save_model_config(model,params)
        )
        
    def _save_model_config(self,model,params):
        result = self._prompt_initializer_manager.save_model_config_by_name(model=model, params=params)
        if result:
            self._speakSystem("prompt_config_successful")
        else:
            self._speakSystem("prompt_config_error")
        self._progressbar.stop()
        
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
