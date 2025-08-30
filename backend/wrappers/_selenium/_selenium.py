from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class SeleniumWrapper():
    def __init__(
        self,
        website :str,
    ):
        # create driver and open website
        self.driver = webdriver.Chrome()
        self.driver.get(website)

    