from .main_page import MainPage
from data.locators import LoginPageLocators
from data.login_data import LoginData


class LoginPage(MainPage):
    def click_login_button(self) -> None:
        self.click_to_element(LoginPageLocators.LOGIN_BTN)

    def click_customer_login_button(self) -> None:
        self.click_to_element(LoginPageLocators.LOGIN_CUSTOMER_BTN)

    def click_login_user(self) -> None:
        self.click_to_element(LoginPageLocators.login_user(LoginData.USER))

    def login_procedure(self) -> None:
        '''
        Кликнули по кнопке Customer Login
        Выбрали Гарри Поттера
        Кликнули по кнопке Login
        '''
        self.click_customer_login_button()
        self.click_login_user()
        self.click_login_button()
