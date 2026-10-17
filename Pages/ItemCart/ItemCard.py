import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ItemCard(BasePage):
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")
    ADD_TO_CARD = (By.ID, "add-to-cart")
    REMOVE = (By.ID, "remove")

    def __init__(self, driver):
        super().__init__(driver)