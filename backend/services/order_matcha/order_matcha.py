import time

from wrappers._selenium._selenium import SeleniumWrapper

from config import URL



def order_matcha() -> None:
    """
    Arguments
    - 

    Returns
    - 
    """
    # --- Create crawler ---
    Crawler = SeleniumWrapper(website=URL)


order_matcha()