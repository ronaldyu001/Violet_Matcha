import logging
from typing import Optional

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement


class SeleniumWrapper():
    def __init__(self, website :str):
        # set up options
        self.options = Options()
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option("useAutomationExtension", False)

        # create driver and open website
        logging.info("Crawler opening website...")
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(website)

    def wait(self):
        """
        Wrapper around WebDriverWait(self.driver, timeout=10)
        """
        return WebDriverWait(driver=self.driver, timeout=10)
    
    def switch(self, iframe: Optional[WebElement], mode: str = ["iframe", "default"]):
        """
        Switch to iframe or default mode. Any argument other than "iframe" will go default.
        """
        if mode == "iframe": self.driver.switch_to.frame(iframe)
        else: self.driver.switch_to.default_content()
