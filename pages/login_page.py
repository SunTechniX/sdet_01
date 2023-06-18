from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def click_login_button(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_BTN).click()

    def click_customer_login_button(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_CUSTOMER_BTN).click()

    def click_login_user_selector(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_USER_SELECT).click()

    def click_login_user(self):
        self.browser.find_element(*LoginPageLocators.LOGIN_USER).click()

    def should_be_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Login Button is not presented"

    def should_be_customer_login_button(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_CUSTOMER_BTN), "Customer Login Button is not presented"

    def should_be_login_user_selector(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER_SELECT), "User Selector DropDownBox is not presented"

    def should_be_login_user(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USER), "User is not presented"
