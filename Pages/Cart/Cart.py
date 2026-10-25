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
    BTN_PRIMARY_ADD_TO_CARD = (By.CLASS_NAME, "btn_primary")
    BTN_SECONDARY_REMOVE = (By.CLASS_NAME, "btn_secondary")
    CART_LIST = (By.CLASS_NAME, "cart_list")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")


    def __init__(self, driver):
        super().__init__(driver)

    def click_checkout_on_cart_page(self):
        self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON)).click()
        return self


    def get_cart_items(self):
        items = self.driver.find_elements(*self.CART_ITEM)
        return items