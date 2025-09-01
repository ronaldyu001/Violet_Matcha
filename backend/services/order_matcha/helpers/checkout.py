import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

from config import CART_URL
from backend.models.users.Violet import Violet
from wrappers._selenium._selenium import SeleniumWrapper


# === helpers ===
def infiltrate_iframe(crawler: SeleniumWrapper, xpath: str, iframe: WebElement, payload: str, clear: bool = True) -> WebElement:
    """
    Finds a target element in an iframe and drops the payload.
    """
    crawler.switch(iframe=iframe, mode="iframe") # switch to iframe
    logging.info("Switched to iframe.")
    target = crawler.wait().until(EC.presence_of_element_located((By.XPATH, xpath)))
    if clear: target.clear()
    target.send_keys(payload)
    crawler.switch(iframe=None, mode="default") # switch to default
    logging.info("Switched to default")

# === checkout ===
def checkout(crawler: SeleniumWrapper):
    try:
        # --- go to cart and create user ---
        logging.info("Going to cart.")
        crawler.driver.get(url=CART_URL)
        user = Violet

        # --- agree to TOS ---
        logging.info("Agreeing to TOS.")
        tos_button = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//input[@id="cart_agree" and @type="checkbox"]'))
        )
        tos_button.click()

        # --- press checkout ---
        logging.info("Proceeding to checkout.")
        checkout_button = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//button[@type="submit" and @name="checkout" and contains(@class, "add_to_cart")]'))
        )
        checkout_button.click()

        # --- enter delivery information ---
        delivery_fields_xpaths = {
            "email": '//input[@placeholder="Email"]',
            "first_name": '//input[@placeholder="First name"]',
            "last_name": '//input[@placeholder="Last name"]',
            "address": '//input[@placeholder="Address"]',
            "city": '//input[@placeholder="City"]',
            "zipcode": '//input[@placeholder="ZIP code"]',
            "phone": '//input[@placeholder="Phone"]'
        }

        # load all delivery fields
        logging.info("Looking for delivery fields.")
        delivery_fields: list[WebElement] = []
        for name, xpath in delivery_fields_xpaths.items():
            delivery_fields.append(crawler.wait().until(
                EC.presence_of_element_located((By.XPATH, xpath))
            ))

        # enter all deliver fields
        logging.info("Entering delivery information.")
        for field, info in zip(delivery_fields, delivery_fields_xpaths.keys()):
            field.clear()
            field.send_keys(user[info])

        # enter state
        state_field = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//select[@name="zone" and @autocomplete="shipping address-level1"]'))
        )
        state_field.click()
        texas_option = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//option[@value="TX" and text()="Texas"]'))
        )
        texas_option.click()

        # --- enter payment information ---
        payment_fields_iframe_xpaths = {
            "card_number": '//iframe[contains(@id, "card-fields-number") and @title="Field container for: Card number"]',
            # "expiration_date": '//iframe[contains(@id, "card-fields-expiry") and @title="Field container for: Expiration date (MM / YY)"]',
            "security_code": '//iframe[contains(@id, "card-fields-verification_value") and @title="Field container for: Security code"]',
            "name_on_card": '//iframe[contains(@id, "card-fields-name") and @title="Field container for: Name on card"]'
        }

        payment_fields_xpaths = {
            "card_number": '//input[@id="number" and @name="number"]',
            # "expiration_date": '//input[@id="expiry" and @name="expiry"]',
            "security_code": '//input[@id="verification_value" and @name="verification_value"]',
            "name_on_card": '//input[@id="name" and @name="name"]',
        }

        payload = {
            "card_number": user["card_number"],
            # "expiration_date": user["expiration_date"],
            "security_code": user["security_code"],
            "name_on_card": user["name_on_card"]
        }

        # get rid of popup
        try: WebDriverWait(driver=crawler.driver, timeout=3).until(EC.presence_of_element_located((By.XPATH, payment_fields_xpaths["card_number"])))
        except: 
            logging.info("Clicking screen.")
            time.sleep(1)
            crawler.driver.find_element(By.TAG_NAME, "body").click()

        # load all payment iframes
        logging.info("Looking for payment iframes.")
        payment_iframes: list[WebElement] = []
        for name, xpath in payment_fields_iframe_xpaths.items():
            # logging.info(f"Looking for iframe: {name}.")
            payment_iframes.append(crawler.wait().until(
                EC.presence_of_element_located((By.XPATH, xpath))
            ))
            # logging.info(f"Found iframe: {name}")

        # enter all payment fields (except expiration date)
        logging.info("Entering payment information.")
        for iframe, info_xpath, load in zip(payment_iframes, payment_fields_xpaths.values(), payload.values()):
            infiltrate_iframe(crawler=crawler, xpath=info_xpath, iframe=iframe, payload=load)

        # enter expiration date field
        exp_date_xpath = '//input[@id="expiry" and @name="expiry"]'
        exp_date_iframe_xpath = '//iframe[contains(@id, "card-fields-expiry") and @title="Field container for: Expiration date (MM / YY)"]'
        payload = user["expiration_date"].split(sep="/")
        exp_date_iframe = crawler.wait().until(EC.presence_of_element_located((By.XPATH, exp_date_iframe_xpath)))
        for load in payload:
            infiltrate_iframe(crawler=crawler, xpath=exp_date_xpath, iframe=exp_date_iframe, payload=load, clear=False)
            time.sleep(2)

        # use same billing as shipping
        same_billing_checkbox = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="checkbox" and @id="billingAddress"]'))
        )
        same_billing_checkbox.click()

        # don't save info (assuming automatically on)
        save_info_button = crawler.wait().until(
            EC.presence_of_element_located((By.XPATH, '//input[@type="checkbox" and @id="RememberMe-RememberMeCheckbox" and @name="RememberMe"]')))
        save_info_button.click()

    except Exception as err:
        logging.error(err)