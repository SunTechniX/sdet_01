from selenium.webdriver.support.color import Color
from .main_page import MainPage
from data.locators import AccountPageLocators


class AccountPage(MainPage):
    def check_welcome_user(self, user_name):
        assert user_name == self.browser.find_element(*AccountPageLocators.ACC_WELCOME_USER).text, "Wrong User Name"

    def check_deposit_success_msg_color(self, color):
        msg = self.browser.find_element(*AccountPageLocators.ACC_DEPOSIT_SUCCESS_MSG)
        msg_css_color = Color.from_string(msg.value_of_css_property('color')).hex
        assert msg_css_color.lower() == color.lower(), "COLOR of Deposit SUCCESS message is NOT EXPECTED!"

    def click_deposit_button(self):
        self.click_to_element(AccountPageLocators.ACC_DEPOSIT_BTN)

    def click_deposit_submit(self):
        self.click_to_element(AccountPageLocators.ACC_DEPOSIT_SUBMIT)

    def click_transactions_button(self):
        self.click_to_element(AccountPageLocators.ACC_TRANSACT_BTN)

    def write_to_deposit_field(self, sn):
        self.browser.find_element(*AccountPageLocators.ACC_AMOUNT_FIELD).send_keys(str(sn))

    def should_be_deposit_button(self):
        assert self.is_element_present(AccountPageLocators.ACC_DEPOSIT_BTN), "Deposit Button is not presented"

    def should_be_amount_field(self):
        assert self.is_element_present(AccountPageLocators.ACC_AMOUNT_FIELD), "Amount Field is not presented"

    def assert_deposit_success_msg(self):
        assert self.is_element_present(AccountPageLocators.ACC_DEPOSIT_SUCCESS_MSG), "Deposit SUCCESS is not presented"

    def assert_welcome(self):
        assert self.is_element_present(AccountPageLocators.ACC_WELCOME_TEXT), "Welcome text is not presented"
