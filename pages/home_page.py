from .main_page import MainPage
from data.locators import LoginPageLocators


class HomePage(MainPage):
    def assert_home_page(self) -> None:
        ''' Проверяет отображение страницы 'Home' '''
        assert self.is_element_present(LoginPageLocators.LOGIN_CUSTOMER_BTN), "Страница 'Home' не отображается!"