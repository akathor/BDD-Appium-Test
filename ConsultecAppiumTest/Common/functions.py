from Common import config
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def OpenApp(host, desire_cap):
    driver = webdriver.Remote(host, desire_cap)
    return driver
# ======================================================================================#


def locate(context, locator_attribute, locator_text):
    possible_locators = ["id", "xpath", "link text", "partial link text", "name", "tag name", "class name",
                         "css selector"]

    if locator_attribute not in possible_locators:
        raise Exception('The locator attribute provided is not in the approved attributes. Or the spelling and format does not match.\
                                The approved attributes are : %s ' % possible_locators)
    wait = WebDriverWait(context.driver, 20)
    screen_locator = config.LOCATORS_Login["Pantalla"]
    wait.until(EC.element_to_be_clickable((By.XPATH, screen_locator)))
    try:
        element = context.driver.find_element(locator_attribute, locator_text)
        return element
    except Exception as e:
        raise Exception(e)
# ======================================================================================#

