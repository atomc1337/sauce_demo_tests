from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.InventoryPage.InventoryPage import InventoryPage
from Pages.base_page import BasePage
#import dotenv

class Login(BasePage):
    #dotenv.load_dotenv()
    USERNAME_INPUT = (By.ID, "user-name")
    USERPASS_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-test="login-button"]')
    USERNAME_ERROR_ICON = (By.CSS_SELECTOR, '#user-name + [data-icon=circle-xmark]')
    USERPASS_ERROR_ICON = (By.CSS_SELECTOR, '#password + [data-icon=circle-xmark]')


    def __init__(self, driver):
        super().__init__(driver)

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.USERPASS_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

        return InventoryPage(self.driver)

    def is_field_are_red_with_error(self, driver):
        self.wait.until(EC.visibility_of_element_located(Login.USERNAME_INPUT))
        self.wait.until(EC.visibility_of_element_located(Login.USERPASS_INPUT))
        red_username = driver.find_element(*Login.USERNAME_INPUT).get_attribute("class").split()
        red_userpass = driver.find_element(*Login.USERPASS_INPUT).get_attribute("class").split()
        return ("error" in red_username, "error" in red_userpass)


    @staticmethod
    def login_with_standard_user(driver):
        login_as_user = Login(driver)
        return login_as_user.login("standard_user", "secret_sauce")

    @staticmethod
    def login_with_locked_out_user(driver):
        login_as_user = Login(driver)
        return login_as_user.login("locked_out_user", "secret_sauce")

    @staticmethod
    def login_with_problem_user(driver):
        login_as_user = Login(driver)
        return login_as_user.login("problem_user", "secret_sauce")

    @staticmethod
    def login_with_performance_glitch_user(driver):
        login_as_user = Login(driver)
        return login_as_user.login("performance_glitch_user", "secret_sauce")

    @staticmethod
    def login_with_error_user(driver):
        login_as_user = Login(driver)
        return login_as_user.login("error_user", "secret_sauce")

    @staticmethod
    def login_with_visual_user(driver):
        login_as_user = Login(driver)
        return login_as_user.login("visual_user", "secret_sauce")


