import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from wrappers._selenium._selenium import SeleniumWrapper
from services.order_matcha.helpers.scroll_until_element import scroll_until_element
from services.order_matcha.helpers.scroll_to_element import scroll_to_element


def goto_matcha_selection(crawler: SeleniumWrapper, button_XPATH: str):
    try:
        # open matcha page
        crawler.driver.get("https://www.thesteepingroom.com/collections/matcha-tea")
        # get matcha container from button xpath
        logging.info("Getting button.")
        button = crawler.wait().until(EC.presence_of_element_located((
            By.XPATH, button_XPATH)))
        # scroll_until_element(crawler=crawler, element=button)
        scroll_to_element(crawler=crawler, element=button)
        
        logging.info("Getting container")
        container = button.find_element(
            By.XPATH, "//div[contains(@class, 'one-third') and contains(@class, 'thumbnail')]")

        # look for price in container
        logging.info("Checking availability of desired matcha.")
        price_div = container.find_element(
            By.XPATH, "//div[contains(@class, 'sold_out')]")

        price_str = price_div.text.strip().lower()
        if price_str == "sold out": raise Exception("Desired matcha is already sold out.")

        # Navigate to Matcha
        logging.info("Desired matcha in stock!")
        button.click()
        logging.info("Navigating to desired matcha.")

    except Exception as err:
        logging.error(f"Failed to navigate to desired matcha selection: {repr(err)}")
