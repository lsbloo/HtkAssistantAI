from core.utils.design.observer.observer import ClientObserver as OptionsObserver
from core.LLMs.htk_llm_factory import setupHtkAssistantModel
from application.ui.main_frame import MainFrame
from core.context.htk_speaker_context_system import HtkSpeakerContextSystemInitializer
from tools.devices.htk_device_restriction import check_network_restriction
from threading import Thread
from core.loader.htk_resource_loader import HtkResourceLoader

def main():
    """Main function to initialize the HtkAssistantAI application.
    This function sets up the terminal appearance, initializes the environment configuration,
    and starts the main application frame."""
    resourceLoader = HtkResourceLoader()
    if check_restrictions():
        interaction_speaker_system()
        resourceLoader.exec(onStartMainFrame=initialize_main_frame)


def check_restrictions():
    return check_network_restriction()


def interaction_speaker_system(key="enviroment_setup"):
    Thread(
        target=HtkSpeakerContextSystemInitializer()
        .getInstance()
        .initialize_system_audio_context,
        args=(key,),
    ).start()


def show_generic_error(frame: MainFrame):
    frame.enabled_input_frame()
    interaction_speaker_system("error")

def initialize_main_frame():
    frame = MainFrame()
    options_observer = OptionsObserver(
        onSuccess=lambda response: setupHtkAssistantModel(
            response=response, callback=lambda res: frame.update_chat(res)
        ),
        onFailure=lambda _: show_generic_error(frame=frame),
    )

    frame.register_observer(options_observer)
    interaction_speaker_system("first_interaction")
    frame.run()
