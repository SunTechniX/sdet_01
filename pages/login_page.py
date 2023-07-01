from .main_page import MainPage
from data.locators import LoginPageLocators


class LoginPage(MainPage):
    def click_login_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_BTN)

    def click_customer_login_button(self):
        self.click_to_element(LoginPageLocators.LOGIN_CUSTOMER_BTN)

    def click_login_user_selector(self):
        self.click_to_element(LoginPageLocators.LOGIN_USER_SELECT)

    def click_login_user(self):
        self.click_to_element(LoginPageLocators.LOGIN_USER)
