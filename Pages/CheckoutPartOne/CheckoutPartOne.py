from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPartOne(BasePage):
    FIRST_NAME_FIELD = (By.ID, "first-name")
    LAST_NAME_FIELD = (By.ID, "last-name")
    POSTAL_CODE_FIELD = (By.ID, "postal-code")
    CANCEL_BUTTON = (By.ID, "cancel")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        super().__init__(driver)

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self

    def click_continue_with_correct_data_on_name_lname_postal(self):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD)).send_keys(self.FIRST_NAME)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME_FIELD)).send_keys(self.LAST_NAME)
        self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE_FIELD)).send_keys(self.POSTAL_CODE)
        self.wait.until(EC.visibility_of_element_located(self.CONTINUE_BUTTON)).click()
        return self
