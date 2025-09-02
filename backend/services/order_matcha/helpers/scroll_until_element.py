import logging
import time

from wrappers._selenium._selenium import SeleniumWrapper
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def scroll_until_element(crawler: SeleniumWrapper, xpath: str, offset: int = 100):
    found = False
    limit = 20
    turn = 1

    try:
        while not found and turn < limit:
            try:
                logging.info("Scrolling.")
                crawler.driver.execute_script(f"window.scrollBy(0, {offset});")
                time.sleep(0.2)

                element = crawler.driver.find_element(By.XPATH, xpath)
                assert element.is_displayed()
                found = True
                logging.info("Scroll successful.")
                return element  # ✅ Return fresh element

            except Exception as err:
                found = False
                turn += 1

    except Exception as err:
        logging.error(f"Scroll failed: {repr(err)}")
        return None