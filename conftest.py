import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options




@pytest.fixture
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-features=PasswordLeakDetection")
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(executable_path="C:\chromedriver-win64\chromedriver.exe", options=chrome_options)
    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )
    yield driver
    driver.quit()
