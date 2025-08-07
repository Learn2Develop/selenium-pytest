from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CheckoutConfirmation:
    def __init__(self, driver):
        self.driver = driver
        self.locatorcheckout = (By.XPATH, "//button[@class='btn btn-success']")
        self.locatorcountry_option = (By.LINK_TEXT, "India")
        self.locatorcountryname = (By.XPATH, "//input[@id='country']")
        self.locatorcheckbox = (By.XPATH, "//label[@for='checkbox2']")
        self.locatorsubmit = (By.XPATH, "//input[@value='Purchase']")
        self.locatormessage = (By.CLASS_NAME, "alert-success")


    def checkout(self):
        self.driver.find_element(*self.locatorcheckout).click()

    def enter_delivery_address(self, country_name):
        self.driver.find_element(*self.locatorcountryname).send_keys(country_name)
        wait = WebDriverWait(self.driver, 5)
        wait.until(expected_conditions.presence_of_element_located(self.locatorcountry_option))
        self.driver.find_element(*self.locatorcountry_option).click()
        self.driver.find_element(*self.locatorcheckbox).click()
        self.driver.find_element(*self.locatorsubmit).click()

    def validate_order(self):
        message = self.driver.find_element(*self.locatormessage)
        print(message.text)