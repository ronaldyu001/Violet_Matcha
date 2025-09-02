import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from wrappers._selenium._selenium import SeleniumWrapper
from services.order_matcha.helpers.scroll_to_element import scroll_to_element


def add_to_cart(crawler: SeleniumWrapper, size: str):
    try:
        size_buttons = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(@value, {size}) and contains(@value, "gram") and contains(@class, "available")]'))
        )
        scroll_to_element(crawler=crawler, element=size_buttons)
        size_buttons.click()
        logging.info("Selected Size.")

        add_button = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//button[@name="add" and contains(@class, "add_to_cart") and @data-label="Add to Cart"]'))
        )
        scroll_to_element(crawler=crawler, element=add_button)
        add_button.click()

        logging.info("Added to cart.")
        time.sleep(1)

    except Exception as err:
        logging.error(f"Failed to add to cart: {repr(err)}")
