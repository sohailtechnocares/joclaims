# utils/helpers.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime


def wait_for_element(driver, locator, timeout=10):
    """
    Wait until an element is visible.
    """
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_and_click(driver, locator, timeout=10):
    """
    Wait for an element to be visible and click it.
    """
    element = wait_for_element(driver, locator, timeout)
    element.click()
    return element

def wait_and_send_keys(driver, locator, text, timeout=10):
    """
    Wait for an element and send text to it.
    """
    element = wait_for_element(driver, locator, timeout)
    element.clear()
    element.send_keys(text)
    return element

def is_text_present(driver, text, timeout=10):
    """
    Check if a specific text is present on the page.
    """
    return WebDriverWait(driver, timeout).until(lambda d: text in d.page_source)


# utils/safe_actions.py
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def safe_click(driver, locator, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
    except ElementClickInterceptedException:
        time.sleep(1)
        element = driver.find_element(*locator)
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        driver.execute_script("arguments[0].click();", element)


def get_current_date(date_format="%d/%m/%Y"):
    """
    Returns current date in the specified format.
    Default: 'DD/MM/YYYY'
    """
    return datetime.now().strftime(date_format)


