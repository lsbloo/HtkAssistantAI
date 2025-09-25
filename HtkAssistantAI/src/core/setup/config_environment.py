
# INITIALIZE THE CONFIGURATION FOR THE ENVIRONMENT
# This file sets up the environment configuration for the HtkAssistantAI application.
import os
from ..extensions.prompt_loading import load_prompt


environments_config = {}

def initialize_environment():
    environments_config['HTK_ASSISTANT_ENV'] = os.environ.get("HTK_ASSISTANT_ENV", 'development')  # Default to development if not set
    environments_config['HTK_ASSISTANT_VERSION'] = os.environ.get("HTK_ASSISTANT_VERSION", "1.0.0")  # Default version if not set
    environments_config['HTK_ASSISTANT_DEBUG'] = os.environ.get('HTK_ASSISTANT_DEBUG', 'False') # Enable debug mode for development
    environments_config['HTK_ASSISTANT_LOG_LEVEL'] = os.environ.get('HTK_ASSISTANT_LOG_LEVEL', 'DEBUG') # Set log level to DEBUG for detailed logs
    environments_config['HTK_ASSISTANT_API_KEY_LLM_GROQ'] = os.environ.get('HTK_ASSISTANT_API_KEY_LLM_GROQ') # Placeholder for API key, should be set securely, set the key for the LLM Groq Service
    environments_config['HTK_ASSISTANT_API_KEY_LLM_CHATGPT'] = os.environ.get('HTK_ASSISTANT_API_KEY_LLM_CHATGPT') # Placeholder for API key, should be set securely, set the key for the LLM ChatGPT Service
    environments_config['HTK_ASSISTANT_API_KEY_LLM_GEMINI'] = os.environ.get('HTK_ASSISTANT_API_KEY_LLM_GEMINI') # Placeholder for API key, should be set securely, set the key for the LLM Gemini Service
    environments_config['HTK_ASSISTANT_STREAM_URL'] = os.environ.get('HTK_ASSISTANT_STREAM_URL')
    environments_config['HTK_ASSISTANT_PROFILE_IMAGE_PATH'] = os.environ.get('HTK_ASSISTANT_PROFILE_IMAGE_PATH', '')
    environments_config['HTK_ASSISTANT_LOG_FILE_PATH'] = os.environ.get('HTK_ASSISTANT_LOG_FILE_PATH', 'htkinfos.log')
   
    if(environments_config['HTK_ASSISTANT_ENV'] == 'development' and environments_config['HTK_ASSISTANT_DEBUG'] == 'True'):
        print("Development environment detected. Debug mode is enabled.")
        print()
        load_prompt("HTK Assistant Environment", timeSleep=2, loadingPercentSimulate=100)  # Simulate loading a development prompt
        print()
        if(environments_config['HTK_ASSISTANT_LOG_LEVEL'] == 'DEBUG'):
            print()
            print('Environments configuration is loaded', environments_config)  # Print the environment configuration for debugging
        
        
        # Define the keys and their corresponding warning messages
        required_keys = {
            'HTK_ASSISTANT_API_KEY_LLM_GROQ': "Warning: HTK_ASSISTANT_API_KEY_LLM_GROQ is not set. Please set it in your environment variables.",
            'HTK_ASSISTANT_API_KEY_LLM_CHATGPT': "Warning: HTK_ASSISTANT_API_KEY_LLM_CHATGPT is not set. Please set it in your environment variables.",
            'HTK_ASSISTANT_API_KEY_LLM_GEMINI': "Warning: HTK_ASSISTANT_API_KEY_LLM_GEMINI is not set. Please set it in your environment variables.",
            'HTK_ASSISTANT_STREAM_URL': "Warning: HTK_ASSISTANT_STREAM_URL is not set. Please set it in your environment variables.",
            'HTK_ASSISTANT_PROFILE_IMAGE_PATH': "Warning: HTK_ASSISTANT_PROFILE_IMAGE_PATH is not set. Please set it in your environment variables.",
        }

        # Iterate through the required keys and check if they are None
        for key, warning_message in required_keys.items():
            if environments_config.get(key) is None:
                print()
                print(warning_message)
                print()
        