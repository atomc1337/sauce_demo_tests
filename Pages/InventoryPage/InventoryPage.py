import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# from Pages.LoginPage.login import Login


class InventoryPage(BasePage):
    ADD_BACKPACK_ITEM_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_ONESIE_ITEM_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    DELETE_BACKPACK_ITEM_BUTTON = (By.ID, "remove-sauce-labs-backpack")
    DELETE_ONESIE_ITEM_BUTTON = (By.ID, "remove-sauce-labs-onesie")
    BURGER_MENU_OPEN_BUTTON = (By.ID, "react-burger-menu-btn")
    BURGER_MENU_LOGOUT = (By.ID, "logout_sidebar_link")
    BURGER_MENU_CLOSE = (By.ID, "react-burger-cross-btn")
    BURGER_MENU = (By.CLASS_NAME, "bm-menu-wrap")
    BURGER_MENU_ALL_ITEMS = (By.ID, "inventory_sidebar_link")
    BURGER_MENU_ABOUT = (By.ID, "about_sidebar_link")
    BURGER_MENU_RESET_APP_STATE = (By.ID, "reset_sidebar_link")
    INVENTORY_LIST = (By.CLASS_NAME, "inventory_list")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    SORT_OPTION_AZ = "az"
    SORT_OPTION_ZA = "za"
    SORT_OPTION_LOHI = "lohi"
    SORT_OPTION_HILO = "hilo"
    INVENTORY_ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    INVENTORY_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    INVENTORY_ITEM = (By.CLASS_NAME, "inventory_item")
    BTN_SECONDARY = (By.CLASS_NAME, "btn_secondary") #кнопка Remove у товара
    BTN_PRIMARY = (By.CLASS_NAME, "btn_primary") #кнопка Add To Card у товара
    INVENTORY_ITEM_IMG = (By.CLASS_NAME, "inventory_item_img") #картинка у товара
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains("inventory.html"))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "page_wrapper")))
        return self

    @staticmethod
    def add_backpack_to_cart(driver):
        add_item = driver.find_element(*InventoryPage.ADD_BACKPACK_ITEM_BUTTON)
        return add_item.click()

    '''@staticmethod
    def delete_backpack_from_cart_on_item_block_button(driver):
        delete_item = driver.find_element(*InventoryPage.DELETE_BACKPACK_ITEM_BUTTON)
        return delete_item.click()'''


    def add_items_to_cart_and_return_objects(self, count=1):
        items_list = self.driver.find_elements(*(self.INVENTORY_ITEM))
        i = 0
        objects = []
        for el in items_list:
            if i == count:
                break
            try:
                self.wait.until(EC.visibility_of(el.find_element(*self.BTN_PRIMARY))).click()
                i += 1
            except:
                continue
            objects.append(el)
        return objects

    @staticmethod
    def add_two_items_to_cart(driver):
        InventoryPage.add_backpack_to_cart(driver)
        InventoryPage.add_items_to_cart_and_return_objects()


    '''@staticmethod
    def delete_onesie_from_cart_on_item_block_button(driver):
        delete_item = driver.find_element(*InventoryPage.DELETE_ONESIE_ITEM_BUTTON)
        return delete_item.click()'''

    @staticmethod
    def open_burger_menu_from_inventory_page(driver):
        base_page_object = BasePage(driver)
        open_menu = base_page_object.wait.until(EC.visibility_of_element_located(InventoryPage.BURGER_MENU_OPEN_BUTTON))
        return open_menu.click()


    @staticmethod
    def logout_from_inventory_page_menu(driver):
        base_page_object = BasePage(driver)
        logout = base_page_object.wait.until(EC.visibility_of_element_located(InventoryPage.BURGER_MENU_LOGOUT))
        return logout.click()

    @staticmethod
    def close_burger_menu_from_inventory_page(driver):
        base_page_object = BasePage(driver)
        close = base_page_object.wait.until(EC.visibility_of_element_located(InventoryPage.BURGER_MENU_CLOSE))
        return close.click()

    @staticmethod
    def click_reset_app_state_button(driver):
        base_page_object = BasePage(driver)
        reset_app_state = base_page_object.wait.until(EC.visibility_of_element_located(InventoryPage.BURGER_MENU_RESET_APP_STATE))
        return reset_app_state.click()

    def get_inventory_items_names(self):
        inventory_items_names = self.driver.find_elements(*self.INVENTORY_ITEM_NAME)
        return [item_names.text for item_names in inventory_items_names]

    def get_inventory_items_price(self):
        inventory_items_prices = self.driver.find_elements(*self.INVENTORY_ITEM_PRICE)
        float_inventory_items_prices = []
        for item_price in inventory_items_prices:
            item_price_float = item_price.text.replace("$", "")
            float_inventory_items_prices.append(float(item_price_float))
        return float_inventory_items_prices

    def click_sort_dropdown(self):
        self.driver.find_element(*self.SORT_DROPDOWN).click()
        #self.driver.find_element(*option).click()
        return self

    def sort_option_selector(self, option):
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, 'product_sort_container'))
        dropdown.select_by_value(option)
        return self #self.driver.find_element(By.CSS_SELECTOR, f"[class='product_sort_container',option_value={option}]").click()


    '''def go_to_sauce_labs_backpack(self):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'inventory_item_name') and text()='Sauce Labs Backpack']"))).click()
        return self'''

    def click_cart_icon_and_go_to_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.SHOPPING_CART_LINK)).click()
        return self


    def get_list_items(self):
        self.wait.until(EC.visibility_of_element_located(self.INVENTORY_ITEM))
        return self.driver.find_elements(*self.INVENTORY_ITEM)

    def get_item_id_on_inventory_page(self, inventory_list):
        name_element = inventory_list.find_element(*self.INVENTORY_ITEM_NAME)
        item_id = str(name_element.find_element(By.XPATH, "./..").get_attribute("id").split("_")[1])
        return item_id

"""    def add_items_to_cart_and_return_objects(self, count=1):
        items_list = self.driver.find_elements(*(self.INVENTORY_ITEM))
        i = 0
        name_price = []
        for el in items_list:
            if i == count:
                break
            el.find_element(By.CLASS_NAME, "btn_inventory").click()
            i += 1
            name_price_tuple = (el.find_element(*self.INVENTORY_ITEM_NAME).text, el.find_element(*self.INVENTORY_ITEM_PRICE).text)
            name_price.append(name_price_tuple)
        return name_price
        
            def add_items_to_cart_and_return_objects(self):
        scroll = ActionChains(self, driver)
        basepage_object = BasePage(driver)
        add_item = basepage_object.wait.until(EC.visibility_of_element_located(InventoryPage.ADD_ONESIE_ITEM_BUTTON))
        scroll.move_to_element(add_item).perform()
        return add_item.click()
        """