import time

def load_prompt(prompt_name, timeSleep = 4, loadingPercentSimulate = 100):    
    """
    Load a prompt from the prompts directory.
    
    Args:
        prompt_name (str): The name of the prompt file to load.
        timeSleep (float): The time to simulate loading in seconds.
        loadingPercentSimulate (int): The percentage of loading to simulate.
        
    Returns:
        str: The content of the prompt file.
    """
    for i in range(loadingPercentSimulate):
        time.sleep(timeSleep / loadingPercentSimulate)  # Simulate loading time
        print(f"Loading {prompt_name}: {i + 1}% complete", end='\r')  # Print loading progress
    