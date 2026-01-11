import argparse
from core.log.htk_logger import HtkApplicationLogger
from core.utils.os_env.os_env import HtkOsEnvironment
from core.setup.config_environment import initialize_environment
import os
import time

class HtkArgs:
    def __init__(self):
        self._logger = HtkApplicationLogger()
        self._parser = argparse.ArgumentParser(
            description="HtkAssistantAI Command Line Interface"
        )
        self._parser.add_argument(
            "--models",
            action="store_true",
            help="List of models to use, are found in environment variables, separated by comma",
        )
        self._parser.add_argument(
            "--verbose", action="store_true", help="Enable verbose output"
        )
        self._parser.add_argument(
            "--init", action="store_true", help="Activate initialization mode"
        )
        self._parser.add_argument(
            "--env", action="store_true", help="Description for environment variables"
        )
        self._parser.add_argument(
            "--doc", action="store_true", help="Show documentation"
        )
        self._args = self._parser.parse_args()
        self._logger.log("HtkAssistantAI Command Line Arguments Initialized and Parsed")

    def exec(self, onInitCallback=None):
        self.init(onInitCallback=onInitCallback)
        self.show_models()
        self.show_env_description()
        self.show_documentation()

    def show_models(self):
        if self._args.models:
            initialize_environment()
            self._logger.log("Listing available models from environment variables...")
            models = HtkOsEnvironment.getModelsAvailableInEnvironment()
            print()
            print("Available Models:", ", ".join(models))

    def init(self, onInitCallback=None):
        if self._args.init:
            self._logger.log("Initialization mode activated.")
            time.sleep(1)  # Simulate some initialization work
            self._logger.log("Initialization complete.")
            onInitCallback()

    def show_env_description(self):
        if self._args.env:
            initialize_environment()
            self._logger.log("Showing environment variables description...")
            os.system("cls" if os.name == "nt" else "clear")
            print("Environment Variables Value:")
            print(
                "--------------------------------------------------------------------------------------------------------------------------------------"
            )
            print("Variable\t       Value")

            # Import the environment configuration dynamically
            from core.setup.config_environment import environments_config
            from core.setup.config_environment import environments_config_description

            # Iterate through the environment variables and print their values
            for variable, value in environments_config.items():
                print(f"{variable}\t{value}")
            print()
            print()
            print()

            print("Environment Variables Description:")
            print(
                "--------------------------------------------------------------------------------------------------------------------------------------"
            )
            print("Variable\t       Description")
            # Iterate through the environment variables and print their descriptions
            for variable, value in environments_config_description.items():
                print(f"{variable}\t{value}")

            print()

    def show_documentation(self):
        if self._args.doc:
            self._logger.log("Showing documentation...")
            print()
            print("HtkAssistantAI Command Line Interface Documentation")
            print(
                "This application is designed to assist users with AI-powered interactions."
            )
            print(
                "For more information, visit the official documentation website. -> www.github.com/lsbloo/HtkAssistantAI"
            )
            print()

            print("Arguments Description:")
            print(
                "--------------------------------------------------------------------------------------------------------------------------------------"
            )
            print("Argument\tDescription")
            print(
                "--models\tLists the models available in the environment variables, separated by commas."
            )
            print("--verbose\tEnables verbose output for detailed logging.")
            print(
                "--init\tActivates initialization mode, initialize the tool in mode graphic."
            )
            print(
                "--doc\tDisplays the documentation for the HtkAssistantAI application."
            )
            print()
            print()
            print("Documentação da Interface de Linha de Comando do HtkAssistantAI")
            print(
                "Esta aplicação é projetada para auxiliar os usuários com interações alimentadas por IA."
            )
            print("Para mais informações, visite o site oficial da documentação.")
            print()
            print("Descrição dos Argumentos:")
            print(
                "--------------------------------------------------------------------------------------------------------------------------------------"
            )
            print("Argumento\tDescrição")
            print(
                "--models\tLista os modelos disponíveis nas variáveis de ambiente, separados por vírgulas."
            )
            print(
                "--verbose\tHabilita a saída detalhada para registros mais completos."
            )
            print(
                "--init\tAtiva o modo de inicialização, inicia a ferramenta em modo gráfico"
            )
            print("--doc\tExibe a documentação da aplicação HtkAssistantAI.")

            print()
            print()
            print(
                "Para mais informações, visite o site do projeto. -> www.github.com/lsbloo/HtkAssistantAI"
            )
