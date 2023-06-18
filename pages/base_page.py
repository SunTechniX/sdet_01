from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        print('==>> open self.url')
        self.browser.get(self.url)

    def is_element_present_silent(self, how, what):
        try:
            self.browser.find_element(how, what)
        except:
            return False
        return True

    def is_element_present_simple(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_element_present(self, how, what, timeout=30):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        except NoSuchElementException:
            return False
        return True

    def click_logout_btn(self):
        self.browser.find_element(*BasePageLocators.LOGOUT_BTN).click()

    def should_be_logout_btn(self):
        assert self.is_element_present(*BasePageLocators.LOGOUT_BTN), "Logout Button is not presented"
