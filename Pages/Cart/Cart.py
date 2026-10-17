import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Cart(BasePage):
    CONTINUE_SHOPPING = (By.NAME, "continue-shopping")
    ONESIE_CART = (By.XPATH, "//*[@class='inventory_item_name' and text()='Sauce Labs Onesie']")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout_on_cart_page(self):
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON)).click()
        return self
