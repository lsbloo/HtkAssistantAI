from core.iot.network.htk_network_check import HtkNetworkCheck
from core.log.htk_logger import HtkApplicationLogger
from core.extensions.prompt_fliget_appearence import setup_terminal_appearence_network_failure
import time
import sys
    
def check_network_restriction():
    logger = HtkApplicationLogger()
    try:
        if not HtkNetworkCheck.is_connected():
            logger.log("Network is not connected")
            setup_terminal_appearence_network_failure()
            time.sleep(2)
            print()
            print("Check your connection internet!")
            sys.exit(0)
            return False
    except:
        return False
    logger.log("Network is connected")
    return True