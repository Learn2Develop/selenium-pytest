from selenium.webdriver.common.by import By
from pageObjects.checkout_confirmation import CheckoutConfirmation
from utils.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locator_product = (By.XPATH, "//div[@class='card h-100']")
        self.locator_shoplink = (By.XPATH, "//a[contains(@href, 'shop')]")
        self.locator_checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def add_to_cart(self, product_name):
        self.driver.find_element(*self.locator_shoplink).click()
        products = self.driver.find_elements(*self.locator_product)
        for product in products:
            name = product.find_element(By.XPATH, "div/h4//a").text
            if name == product_name:
                product.find_element(By.XPATH, "div/button").click()
                break


    def go_to_cart(self):
        self.driver.find_element(*self.locator_checkout).click()
        checkout = CheckoutConfirmation(self.driver)
        return checkout