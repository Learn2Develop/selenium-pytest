import json

import pytest

from pageObjects.login import LoginPage

test_data_path = "data\\test_e2eframework.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.testrail_case_id(1)
@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browser, test_list_item):
    driver = browser
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    login_page = LoginPage(driver)
    print(login_page.getTitle())
    shop_page = login_page.login(test_list_item["userEmail"], test_list_item["userPassword"])
    print(shop_page.getTitle())
    shop_page.add_to_cart(test_list_item["productName"])
    checkout_confirmation = shop_page.go_to_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()



