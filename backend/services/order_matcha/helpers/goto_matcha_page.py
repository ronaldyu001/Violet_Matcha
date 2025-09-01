import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from wrappers._selenium._selenium import SeleniumWrapper




def goto_matcha_page(crawler: SeleniumWrapper):
    try:
        # Open TEAS dropdown
        logging.info("Opening TEAS dropdown.")
        teas_dropwdown = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-sections--19959238295775__header"]/header[2]/div/div[3]/div/div[2]/div[1]/nav[1]/ul/li[1]/details/summary')))
        action = ActionChains(crawler.driver)
        action.move_to_element(teas_dropwdown).perform()

        # Navigate to Matcha
        logging.info("Navigating to Matcha Shop.")
        matcha_page = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="shopify-section-sections--19959238295775__header"]/header[2]/div/div[3]/div/div[2]/div[1]/nav[1]/ul/li[1]/details/div/div/div[2]/div[2]/a/p')))
        matcha_page.click()

    except Exception as err:
        logging.error(f"Failed to navigate to matcha page: {repr(err)}")