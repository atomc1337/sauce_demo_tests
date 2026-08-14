import time
import click
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from conftest import driver

object_of_basepage = BasePage(driver)
print(object_of_basepage.CHECKOUT_COMPLETE_URL.split('com', 1)[1])

""""
@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser


#service = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=service)

def login_test(browser):
    browser.get("https://www.saucedemo.com/")
    input_login = browser.find_element(By.ID, "user-name")
    input_login.send_keys("standard_user")
    time.sleep(2)

    input_password = browser.find_element(By.NAME, "password")
    input_password.send_keys("secret_sauce")
    time.sleep(2)

    ok_button = browser.find_element(By.CSS_SELECTOR, "[data-test='login-button']")
    ok_button.click()
    time.sleep(2)

    assert browser.current_url == 'https://www.saucedemo.com/inventory.html', "url is not valid"
    page_wrapper = browser.find_element(By.CLASS_NAME, 'page_wrapper')
    assert page_wrapper.is_displayed(), 'element not found'

# driver.quit()
"""