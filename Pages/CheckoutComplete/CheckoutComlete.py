import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from Pages.LoginPage.Login import Login
from Pages.base_page import BasePage
from Pages.InventoryPage.InventoryPage import InventoryPage
from selenium.webdriver.support.wait import WebDriverWait
from Pages.Cart.Cart import Cart
from Pages.CheckoutPartOne.CheckoutPartOne import CheckoutPartOne
import pdb
from Pages.CheckoutPartTwo.CheckOutPartTwo import CheckoutPartTwo

class CheckoutComplete(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    BACK_HOME_BUTTON = (By.ID, "back-to-products")
    GENERATE_PDF_ORDER = (By.ID, "generate-pdf-order")


    def click_back_home(self):
        self.wait.until(EC.visibility_of_element_located(self.BACK_HOME_BUTTON)).click()
        return self

    def click_generate_pdf_order(self):
        self.wait.until(EC.visibility_of_element_located(self.GENERATE_PDF_ORDER)).click()
        return self