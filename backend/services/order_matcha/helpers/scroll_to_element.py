import logging
import time

from wrappers._selenium._selenium import SeleniumWrapper
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def scroll_to_element(crawler: SeleniumWrapper, element: WebElement, offset: int = 0):
    try:
        logging.info("Scrolling to element.")
        script = "arguments[0].scrollIntoView({ block: 'center', inline: 'nearest' });"
        crawler.driver.execute_script(script, element)
        time.sleep(0.5)
        
        logging.info("Additional scroll.")
        script = f"window.scrollBy(0, {offset});"
        crawler.driver.execute_script(script)
        time.sleep(0.5)

        assert element.is_displayed(), "Element not visible after scrolling"
        logging.info("Scroll successful.")

    except Exception as err:
        logging.error(f"Scroll failed: {repr(err)}")