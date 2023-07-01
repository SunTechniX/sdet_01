import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_Chrome

from data.link_data import LinkData


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store', default='false',
                     help="Open a browser invisible, without GUI is used by default")

@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption('headless')
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = Options_Chrome()        #
        if headless == 'true':
            chrome_options.add_argument('headless')
        chrome_options.add_argument("--window-size=1350,800")
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        if headless == 'true':
            os.environ['MOZ_HEADLESS'] = '1'
        firefox_profile = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=firefox_profile)
        browser.implicitly_wait(5)
    elif browser_name == "hub":
        browser = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities={"browserName": "chrome", 'javascriptEnabled': True})
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or hub")
    browser.get(LinkData.LINK)
    yield browser
    browser.quit()
