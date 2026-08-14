from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.base_page import BasePage


class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_to_load(self):
        WebDriverWait(self.driver, 5).until(EC.url_contains("inventory.html"))
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "page_wrapper")))
        return self


