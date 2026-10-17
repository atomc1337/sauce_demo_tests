from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.LoginPage.Login import Login
from Pages.InventoryPage.InventoryPage import InventoryPage
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Cart.Cart import Cart
from Pages.CheckoutPartOne.CheckoutPartOne import CheckoutPartOne
import pdb
class CheckoutPartTwo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")


    def click_cancel_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CANCEL_BUTTON)).click()
        return self

    def click_finish_button(self):
        self.wait.until(EC.visibility_of_element_located(self.FINISH_BUTTON)).click()
        return self

    def click_item_name_and_go_to_item_card(self):
        self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME)).click()
        return self

