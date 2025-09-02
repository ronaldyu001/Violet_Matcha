import time

from wrappers._selenium._selenium import SeleniumWrapper
from services.order_matcha.helpers.scroll_to_element import scroll_to_element
from services.order_matcha.helpers.scroll_until_element import scroll_until_element

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


def increase_amount(crawler: SeleniumWrapper, container: WebElement):
    try:
        plus_button = container.find_element(By.XPATH, ".//span[contains(@class, 'icon-plus')]")
        # plus_button = scroll_until_element(crawler=crawler, xpath=plus_button_xpath)
        plus_button.click()

    except Exception as err:
        raise Exception(err)