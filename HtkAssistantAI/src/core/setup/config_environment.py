
# INITIALIZE THE CONFIGURATION FOR THE ENVIRONMENT
# This file sets up the environment configuration for the HtkAssistantAI application.
import os
from ..extensions.prompt_loading import load_prompt


environments_config = {}

def initialize_environment():
    environments_config['HTK_ASSISTANT_ENV'] = os.environ.get("HTK_ASSISTANT_ENV", 'development')  # Default to development if not set
    environments_config['HTK_ASSISTANT_VERSION'] = os.environ.get("HTK_ASSISTANT_VERSION", "1.0.0")  # Default version if not set
    environments_config['HTK_ASSISTANT_DEBUG'] = os.environ.get('HTK_ASSISTANT_DEBUG', 'True') # Enable debug mode for development
    environments_config['HTK_ASSISTANT_LOG_LEVEL'] = os.environ.get('HTK_ASSISTANT_LOG_LEVEL', 'DEBUG') # Set log level to DEBUG for detailed logs
    environments_config['HTK_ASSISTANT_API_KEY_LLM_GROQ'] = os.environ.get('HTK_ASSISTANT_API_KEY_LLM_GROQ') # Placeholder for API key, should be set securely, set the key for the LLM Groq Service
    if(environments_config['HTK_ASSISTANT_ENV'] == 'development' and environments_config['HTK_ASSISTANT_DEBUG'] == 'True'):
        print("Development environment detected. Debug mode is enabled.")
        load_prompt("HTK Assistant Environment", timeSleep=2, loadingPercentSimulate=100)  # Simulate loading a development prompt
        if(environments_config['HTK_ASSISTANT_LOG_LEVEL'] == 'DEBUG'):
            print('Environments configuration is loaded', environments_config)  # Print the environment configuration for debugging
        
        if(environments_config['HTK_ASSISTANT_API_KEY_LLM_GROQ'] is None):
            print()
            print("Warning: HTK_ASSISTANT_API_KEY_LLM_GROQ is not set. Please set it in your environment variables.")
            print()
        