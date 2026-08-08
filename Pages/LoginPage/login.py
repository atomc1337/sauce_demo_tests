from selenium.webdriver.common.by import By

from Pages.InventoryPage.InventoryPage import InventoryPage
from Pages.base_page import BasePage
class Login(BasePage):
    
    ERROR_ICON = (By.CSS_SELECTOR, '[data-icon="circle-xmark"]')
    USERNAME_INPUT = (By.ID, "user-name")
    USERPASS_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.USERPASS_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

        return InventoryPage(self.driver)
