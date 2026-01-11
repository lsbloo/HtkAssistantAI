from pyfiglet import Figlet

# This file sets up the terminal appearance for the HtkAssistantAI application.
def setup_terminal_appearance():
    """
    Set up the terminal appearance with custom ASCII art and text.
    """
    f = Figlet(font="slant")
    print(f.renderText("HtkAssistantAI"))


def setup_terminal_appearence_network_failure():
    """
    Set up the terminal appearance with network error custom ASCII art and text.
    """
    f = Figlet(font="slant")
    print(f.renderText("ERROR NETWORK"))
