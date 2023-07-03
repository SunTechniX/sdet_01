from selenium.webdriver.support.color import Color
from .main_page import MainPage
from data.account_data import AccountData
from data.locators import AccountPageLocators
from data.login_data import LoginData


class AccountPage(MainPage):
    def account_procedure(self) -> None:
        '''
        Выполнить операцию пополнения счета на 100 единиц валюты
        Проверить что сообщение Deposit Successful красного цвета
        Нажать на кнопку "Transactions"
        '''
        self.compare_welcome_user(LoginData.USER)
        self.click_deposit_button()
        self.write_to_deposit_field(AccountData.AMOUNT)
        self.click_deposit_submit()
        self.assert_deposit_success_msg_color(AccountData.COLOR)
        self.click_transactions_button()

    def assert_deposit_success_msg_color(self, color: str) -> None:
        ''' проверка цвета color с цветом надписи на странице '''
        msg = self.browser.find_element(*AccountPageLocators.ACC_DEPOSIT_SUCCESS_MSG)
        msg_css_color = Color.from_string(msg.value_of_css_property('color')).hex
        assert msg_css_color.lower() == color.lower(), "COLOR of Deposit SUCCESS message is NOT EXPECTED!"

    def compare_welcome_user(self, user_name) -> None:
        ''' Сравнить имя пользователя user_name с именем в приглашении странницы '''
        self.equal_element_text(AccountPageLocators.ACC_WELCOME_USER, user_name)

    def click_deposit_button(self) -> None:
        self.click_to_element(AccountPageLocators.ACC_DEPOSIT_BTN)

    def click_deposit_submit(self) -> None:
        self.click_to_element(AccountPageLocators.ACC_DEPOSIT_SUBMIT)

    def click_transactions_button(self) -> None:
        self.click_to_element(AccountPageLocators.ACC_TRANSACT_BTN)

    def write_to_deposit_field(self, amount: int) -> None:
        ''' Записать в элемент сумму пополнения amount '''
        self.write_to_element(AccountPageLocators.ACC_AMOUNT_FIELD, str(amount))
