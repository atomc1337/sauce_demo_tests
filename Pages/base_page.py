from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=5):
        self.wait = WebDriverWait(driver, timeout)
        self.driver = driver

