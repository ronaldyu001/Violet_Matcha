import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from wrappers._selenium._selenium import SeleniumWrapper


def add_to_cart(crawler: SeleniumWrapper, size: str):
    try:
        logging.info("Selecting Size.")
        size_buttons = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, f'//div[contains(@value, {size}) and contains(@value, "gram") and contains(@class, "available")]'))
        )
        size_buttons.click()

        logging.info("Adding to cart.")
        add_button = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//button[@name="add" and contains(@class, "add_to_cart") and @type="submit"]'))
        )

        
        add_button.click()

    except Exception as err:
        logging.error(f"Failed to add to cart: {repr(err)}")
        raise Exception(err)