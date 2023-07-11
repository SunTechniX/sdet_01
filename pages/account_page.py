from selenium.webdriver.support.color import Color

from .main_page import MainPage
from data.locators import AccountPageLocators


class AccountPage(MainPage):
    def compare_deposit_success_msg_color(self, color: str) -> None:
        ''' Проверяет цвет color с цветом надписи на странице '''
        msg = self.browser.find_element(*AccountPageLocators.ACC_DEPOSIT_SUCCESS_MSG)
        msg_css_color = Color.from_string(msg.value_of_css_property('color')).hex
        assert msg_css_color.lower() == color.lower(), "Цвет сообщения Deposit Successful не соответствует ожидаемому!"

    def compare_welcome_user(self, user_name) -> None:
        ''' Сравнивает имя пользователя user_name с именем в приглашении странницы '''
        self.compare_element_text(AccountPageLocators.ACC_WELCOME_USER, user_name)

    def click_btn_name(self, name_btn: str) -> None:
        ''' Нажимаеть на кнопку name_btn '''
        self.click_to_element(AccountPageLocators.button_name(name_btn))

    def click_deposit_submit(self) -> None:
        ''' Нажимаеть на кнопку "Submit" '''
        self.click_to_element(AccountPageLocators.ACC_DEPOSIT_SUBMIT)

    def write_to_deposit_field(self, amount: int) -> None:
        ''' Выполнить операцию пополнения счета на amount единиц валюты '''
        self.write_to_element(AccountPageLocators.ACC_AMOUNT_FIELD, str(amount))
