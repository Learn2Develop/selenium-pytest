import sys
import time
import config
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class driverClass:
    def __init__(self, url):
        self.url = url
        self.chromeoptions = config.chromeoptions
        try:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_experimental_option("detach", True)
            my_dir = {"download.default_directory": "C:\\Users\\amank\\Documents", "safebrowsing.enabled": "false"}
            chrome_options.add_experimental_option("prefs", my_dir)
            chrome_options.add_argument("--ignore-certificate-errors")
            for option in self.chromeoptions:
                chrome_options.add_argument(option)
            service_obj = Service("C:\\Users\\amank\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
            self.driver = webdriver.Chrome(service=service_obj, options=chrome_options)
            self.driver.get(self.url)
            self.driver.maximize_window()
        except:
            print("Browser instantiation failed. Error occurred: {}".format(sys.exc_info()))

        time.sleep(2)

    def get_driver(self):
        return self.driver
