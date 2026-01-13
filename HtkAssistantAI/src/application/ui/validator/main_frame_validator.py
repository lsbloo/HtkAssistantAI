from threading import Thread
from ..utils import show_toast
from core.log.htk_logger import HtkApplicationLogger
from core.context.htk_speaker_context_system import HtkSpeakerContextSystemInitializer


class HtkMainFrameUIValidator:

    def __init__(self,root,isSpeakSystem):
        self._parent_root = root
        self._isSpeakSystem = isSpeakSystem
        self._systemSpeaker = HtkSpeakerContextSystemInitializer().getInstance()
        self._logger = HtkApplicationLogger()
        self._logger.log("Main Frame Validator is initialized")

    def validate_inputs_recon(self, isSpeakSystem, params) -> bool:
        self._isSpeakSystem = isSpeakSystem
        if (
            params.get("selected_model") in ("Selecione um modelo", "No models available")
        ):
            self._logger_failure("validate_inputs_recon", "selected_model")
            return self._speakSystemOrToast("input_validator_error_selected_model")
        elif (
            params.get('selected_option') not in ("simple_chat", "chat_with_roles")
        ):
            self._logger_failure("validate_inputs_recon", "selected_option")
            return self._speakSystemOrToast("input_validator_error_selected_option")
        
        elif (
            params.get("input_from_recon") == ""
            or params.get("input_from_recon") == None
        ):
            self._logger_failure("validate_inputs_recon", "input_from_recon")
            return self._speakSystemOrToast("input_validator_error_input_area")
        else:
            self._logger_successful("validate_inputs_recon")
            return True

    def validate_inputs(self, isSpeakSystem, params) -> bool:
        self._isSpeakSystem = isSpeakSystem
        if (
            params.get("selected_model") in ("Selecione um modelo", "No models available")
        ):
            self._logger_failure("validate_inputs", "selected_model")
            return self._speakSystemOrToast("input_validator_error_selected_model")

        
        elif (
            params.get('selected_option') not in ("simple_chat", "chat_with_roles")
        ):
            self._logger_failure("validate_inputs", "selected_option")
            return self._speakSystemOrToast("input_validator_error_selected_option")
        
        elif params.get("user_input") == "" or params.get("user_input") == None:
            self._logger_failure("validate_inputs", "user_input")
            return self._speakSystemOrToast("input_validator_error_input_area")
        
        else:
            self._logger_successful("validate_inputs")
            return True

    def _logger_successful(self, method):
        self._logger.log(
            f"Main Frame Validator is {method} has successful validation inputs"
        )

    def _logger_failure(self, method, parameter):
        self._logger.log(
            f"Main Frame Validator is {method} and {parameter} has error in validation inputs"
        )

    def _speakSystemOrToast(self, key):
        if self._isSpeakSystem == True:
            thread = Thread(
                target=self._systemSpeaker.initialize_system_audio_context, args=(key,)
            )
            thread.start()
        else:
            show_toast(
                parent= self._parent_root,
                message = self._systemSpeaker.load_context_system_audio(key=key), duration=3000
            )

        return False
