import time
import logging

from wrappers._selenium._selenium import SeleniumWrapper

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from services.order_matcha.config import URL, MATCHA_XPATH, TEST
from services.order_matcha.helpers.goto_matcha_page import goto_matcha_page
from services.order_matcha.helpers.goto_matcha_selection import goto_matcha_selection
from services.order_matcha.helpers.add_to_cart import add_to_cart
from services.order_matcha.helpers.checkout import checkout
from services.order_matcha.helpers.increase_amount import increase_amount
from services.order_matcha.helpers.scroll_to_element import scroll_to_element



MATCHA = TEST


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def order_matcha(orders: list[dict]) -> None:
    """
    Arguments
    - orders: dict["name": str, "quantity": str]

    Returns
    - 
    """
    try:
        # --- create crawler and go to matcha shop ---
        logging.info("Creating crawler.")
        crawler = SeleniumWrapper(website=URL)

        logging.info("Navigating to Matcha Shop.")
        goto_matcha_page(crawler=crawler)

        # --- for each item, go to shop and add to cart ---
        is_cart_empty = True

        for order in orders:
            # select desired matcha
            logging.info("Navigating to desired matcha.")
            goto_matcha_selection(crawler=crawler, button_XPATH=MATCHA[order["name"]]["button"])
            # goto_matcha_selection(crawler=crawler, price_XPATH=MATCHA_XPATH[order["name"]]["price"], button_XPATH=MATCHA_XPATH[order["name"]]["button"])

            # select quantity
            try:
                logging.info("Getting quantity.")
                increase = bool(int(order["quantity"]) - 1)
                
                # increase quantity
                if increase:
                    logging.info("Increasing quantity.")
                    container = crawler.wait().until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "purchase-details")]')))
                    for _ in range(1, int(order["quantity"])): increase_amount(crawler=crawler, container=container)
            except Exception as err:
                logging.error(repr(err))
                
            # add to cart
            try: 
                add_to_cart(crawler=crawler, size=MATCHA[order["name"]]["quantity"])
                is_cart_empty = False
            except: pass

        # checkout
        if is_cart_empty: raise Exception("Unable to add any of the items. Aborting.")
        logging.info("Checking out.")
        checkout(crawler=crawler)

        # success!
        logging.info("Order placed!")
        crawler.driver.close()
        return

    except Exception as err:
        logging.error(f"Failed to order matcha: {repr(err)}")
        crawler.driver.close()
        raise Exception(err)