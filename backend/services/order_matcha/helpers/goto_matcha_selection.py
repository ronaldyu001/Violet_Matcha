import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


from wrappers._selenium._selenium import SeleniumWrapper




def goto_matcha_selection(crawler: SeleniumWrapper, price_XPATH: str, button_XPATH: str):
    try:
        # Select desired matcha
        logging.info("Checking availability of desired matcha.")
        price_div = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, price_XPATH))
        )
        price_str = price_div.text.strip().lower()
        if price_str == "sold out": raise Exception("Desired matcha is already sold out.")

        # Navigate to Matcha
        logging.info("Desired matcha in stock! Navigating.")
        desired_matcha = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, button_XPATH)))
        desired_matcha.click()

    except Exception as err:
        logging.error(f"Failed to navigate to desired matcha selection: {repr(err)}")