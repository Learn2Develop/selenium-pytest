import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.testrail_api import Testrail_api
import time


# Use a global variable to hold the run_id for the session
RUN_ID = None

driver = None

tr_api = Testrail_api()
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="browser to run test"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "testrail_case_id(id): mark test with TestRail Case ID")

def pytest_sessionstart(session):
    # Hardcode or collect test case IDs for this example
    test_case_ids = [1]
    global RUN_ID
    RUN_ID = tr_api.create_test_run(name="Pytest Automated Run", case_ids=test_case_ids)["id"]
    print(f"\n[TestRail] Created test run: {RUN_ID}")
    tr_api.add_result_for_case(RUN_ID, test_case_ids[0], "passed", "PASSED")

# def pytest_sessionfinish(session, exitstatus):
#     if RUN_ID:
#         tr_api.close_test_run(RUN_ID)
#         print(f"\n[TestRail] Closed test run: {RUN_ID}")


@pytest.fixture(scope='function')
def browser(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    service_obj = Service()
    if browser_name == "chrome":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        # chrome_options.add_argument("--ignore-certificate-errors")
        # chrome_options.add_argument("--disable-infobars")
        # chrome_options.add_experimental_option("prefs", {
        #     "credentials_enable_service": False,
        #     "profile.password_manager_enabled": False
        # })
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
        driver.implicitly_wait(2)
        driver.maximize_window()

    elif browser_name == "edge":
        driver = webdriver.Edge(service=service_obj)
        driver.implicitly_wait(3)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=service_obj)
        driver.implicitly_wait(2)
    yield driver
    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call" or report.when == 'setup':
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # Assuming your screenshot is saved correctly at the specified path
            reports_dir = os.path.join(os.path.dirname(__file__), 'reports')
            file_name = os.path.join(reports_dir, report.nodeid.replace("::", "_") + ".png")
            print("File name is " + file_name)
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(filename):
    driver.get_screenshot_as_file(filename)