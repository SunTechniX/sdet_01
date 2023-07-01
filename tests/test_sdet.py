import pytest

from data.login_data import LoginData
from pages.login_page import LoginPage
from data.account_data import AccountData
from pages.account_page import AccountPage
from pages.trans_page import TransPage


@pytest.mark.harry_potter
class TestHarryPotter:
    def test_harry_potter(self, browser):
        browser.delete_all_cookies()

        login_page = LoginPage(browser)

        login_page.click_customer_login_button() # Кликнули по кнопке Customer Login
        #login_page.should_be_login_user_selector()
        #login_page.click_login_user_selector() # Кликнули по выпадающему списку
        login_page.click_login_user()  # Выбрали Гарри Поттера - user_name напрямую вписан в locators
        login_page.click_login_button()  # Кликнули по кнопке Login

        account_page = AccountPage(browser)
        account_page.assert_welcome()
        account_page.check_welcome_user(LoginData.USER)
        account_page.should_be_deposit_button()
        account_page.click_deposit_button()
        account_page.should_be_amount_field()
        account_page.write_to_deposit_field(AccountData.AMOUNT)
        account_page.click_deposit_submit()
        account_page.assert_deposit_success_msg()
        account_page.check_deposit_success_msg_color('#FF0000') # RED COLOR!!!
        account_page.click_transactions_button()

        trans_page = TransPage(browser)
        trans_page.should_be_trans_table()

        trans_page.should_be_trans_cell_date() # <<<<<<<<<< null table
        trans_page.check_trans_cell_date()
        trans_page.should_be_trans_cell_amount()
        trans_page.check_trans_cell_amount(AccountData.AMOUNT)

        trans_page.click_logout_btn()
        trans_page.click_home_btn()

