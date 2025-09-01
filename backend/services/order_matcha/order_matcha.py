import time
import logging

from config import URL, MATCHA_TO_XPATH
from wrappers._selenium._selenium import SeleniumWrapper
from services.order_matcha.helpers.goto_matcha_page import goto_matcha_page
from services.order_matcha.helpers.goto_matcha_selection import goto_matcha_selection
from services.order_matcha.helpers.add_to_cart import add_to_cart
from services.order_matcha.helpers.checkout import checkout


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def order_matcha() -> None:
    """
    Arguments
    - 

    Returns
    - 
    """
    try:
        # create crawler
        logging.info("Creating crawler...")
        crawler = SeleniumWrapper(website=URL)

        # go to matcha shop
        logging.info("Attempting to navigate to Matcha Shop.")
        goto_matcha_page(crawler=crawler)

        # select desired matcha
        logging.info("Navigating to desired matcha.")
        goto_matcha_selection(crawler=crawler, price_XPATH=MATCHA_TO_XPATH["test_2"]["price"], button_XPATH=MATCHA_TO_XPATH["test_2"]["button"])

        # add to cart
        logging.info("Adding to matcha to cart.")
        add_to_cart(crawler=crawler, size="30")

        # checkout
        logging.info("Checking out.")
        checkout(crawler=crawler)

    except Exception as err:
        logging.error(f"Failed to order matcha: {repr(err)}")

    time.sleep(60)


order_matcha()