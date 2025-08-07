from selenium.webdriver.common.by import By
from pageObjects.shopPage import ShopPage
from utils.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator_username = (By.ID, "username")
        self.locator_password = (By.ID, "password")
        self.locator_terms = (By.ID, "terms")
        self.locator_signin = (By.ID, "signInBtn")


    def login(self, username, password):
        self.driver.find_element(*self.locator_username).send_keys(username)
        self.driver.find_element(*self.locator_password).send_keys(password)
        self.driver.find_element(*self.locator_terms).click()
        self.driver.find_element(*self.locator_signin).click()
        shop_page = ShopPage(self.driver)
        return shop_page
