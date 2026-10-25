import math

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
from decimal import Decimal, ROUND_CEILING

class CheckoutPartTwo(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEMS_PRICE_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    PRICE_TOTAL = (By.CLASS_NAME, "summary_total_label")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def click_cancel_button(self):
        self.wait.until(EC.visibility_of_element_located(self.CANCEL_BUTTON)).click()
        return self

    def click_finish_button(self):
        self.wait.until(EC.visibility_of_element_located(self.FINISH_BUTTON)).click()
        return self

    def click_item_name_and_go_to_item_card(self):
        self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME)).click()
        return self



    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEM)

    def get_clean_items_price(self, items_prices):
        float_inventory_items_prices = []
        if not isinstance(items_prices, list):
            items_prices = [items_prices]
        for item_price in items_prices:
            item_price_float = item_price.text.replace("$", "")
            float_inventory_items_prices.append(float(item_price_float))
        return float_inventory_items_prices

    def get_clean_items_price_total(self, items):
        default_total = self.driver.find_element(*self.ITEMS_PRICE_TOTAL).text
        return float(default_total.split("$")[1])

    def items_price_summ(self, items_prices):
        items_price_summ = 0
        if not items_prices is list:
            items_prices = [items_prices]
        for item in items_prices:
            items_price_summ += items_price_summ + item
        return items_price_summ

    def get_clean_items_tax(self, items_sum):
        num = (items_sum / 100 ) * 8
        return round(num, 1)

    def get_tax(self):
        text = self.driver.find_element(*self.TAX).text
        #fin_t = text.text()
        return float(text.split("$")[1])

    def get_sum(self):
        return float(self.driver.find_element(*self.ITEMS_PRICE_TOTAL).text.split("$")[1])

    def get_total_price_final(self):
        return float(self.driver.find_element(*self.PRICE_TOTAL).text.split("$")[1])