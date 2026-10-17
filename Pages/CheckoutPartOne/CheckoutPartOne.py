from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


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
        self.driver.find_element(*self.FIRST_NAME_FIELD).send_keys(self.FIRST_NAME)
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(self.LAST_NAME)
        self.driver.find_element(*self.POSTAL_CODE_FIELD).send_keys(self.POSTAL_CODE)
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        return self
