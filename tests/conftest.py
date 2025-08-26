import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options_Chrome

from selene import browser
from selene.support.shared import config

from data.link_data import LinkData


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store', default='false',
                     help="Open a browser invisible, without GUI is used by default")

@pytest.fixture
def browser_fixture(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption('headless')
    browser_drv = None
    if browser_name == "chrome":
        chrome_options = Options_Chrome()        #
        if headless == 'true':
            chrome_options.add_argument('headless')
        chrome_options.add_argument("--window-size=1350,800")
        browser_drv = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        if headless == 'true':
            os.environ['MOZ_HEADLESS'] = '1'
        firefox_profile = webdriver.FirefoxProfile()
        browser_drv = webdriver.Firefox(firefox_profile=firefox_profile)
        browser_drv.implicitly_wait(5)
    elif browser_name == "hub":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.capabilities["browserName"] = "chrome"
        chrome_options.browser_version = "128.0"
        browser_drv = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=chrome_options)
            # desired_capabilities={"browserName": "chrome",
            #                       "browserVersion"
            #                       'javascriptEnabled': True})
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or hub")
    browser_drv.get(LinkData.LINK)
    yield browser_drv
    browser_drv.quit()


@pytest.fixture
def browser_selene(request):
    browser_name = request.config.getoption("browser_name")
    headless = request.config.getoption('headless')
    browser_drv = None
    if browser_name == "chrome":
        chrome_options = Options_Chrome()        #
        if headless == 'true':
            chrome_options.add_argument('headless')
        chrome_options.add_argument("--window-size=1350,800")
        browser_drv = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        if headless == 'true':
            os.environ['MOZ_HEADLESS'] = '1'
        firefox_profile = webdriver.FirefoxProfile()
        browser_drv = webdriver.Firefox(firefox_profile=firefox_profile)
        browser_drv.implicitly_wait(5)
    elif browser_name == "hub":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-gpu")
        chrome_options.capabilities["browserName"] = "chrome"
        chrome_options.browser_version = "128.0"
        browser_drv = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            options=chrome_options)
            # desired_capabilities={"browserName": "chrome",
            #                       "browserVersion"
            #                       'javascriptEnabled': True})
    else:
        raise pytest.UsageError("--browser_name should be chrome, firefox or hub")

    browser.config.driver = browser_drv  # selene
    browser_drv.get(LinkData.LINK)
    yield browser_drv
    browser_drv.quit()


@pytest.fixture
def browser_del_cookie(browser_fixture):
    browser_fixture.delete_all_cookies()


@pytest.fixture
def selene_del_cookie(browser_selene):
    browser_selene.delete_all_cookies()
