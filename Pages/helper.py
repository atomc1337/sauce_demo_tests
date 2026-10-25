import time
from Pages.LoginPage.Login import Login
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage

class Helper(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    def check_pages_to_go(self, driver, url):
        object_of_login = Login(driver)
        time.sleep(1)
        object_of_login.driver.get(url)
        endpoint_to_message = (object_of_login.CHECKOUT_COMPLETE_URL.split('.com', 1)[1])
        assert object_of_login.wait.until(EC.url_contains("https://www.saucedemo.com/"))
        assert object_of_login.is_field_are_red_with_error(driver) == (True, True)
        assert EC.text_to_be_present_in_element(object_of_login.ERROR_MESSAGE_CONTAINER, f"Epic sadface: You can only access '{endpoint_to_message}' when you are logged in.")
        assert object_of_login.driver.find_element(*object_of_login.USERNAME_ERROR_ICON).is_displayed()
        assert object_of_login.driver.find_element(*object_of_login.USERPASS_ERROR_ICON).is_displayed()