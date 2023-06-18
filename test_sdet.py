# pytest -v -s -m harry_potter test_sdet.py
# pytest -v -s test_sdet.py

import pytest
from .pages.login_page import LoginPage
from .pages.account_page import AccountPage
from .pages.trans_page import TransPage

LINK = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"

@pytest.mark.harry_potter
class TestHarryPotter():
    link = LINK

    def test_harry_potter(self, browser):
        browser.delete_all_cookies()
        user_name = 'Harry Potter'
        amount = 100
        link = LINK
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.should_be_customer_login_button()
        login_page.click_customer_login_button() # Кликнули по кнопке Customer Login
        #login_page.should_be_login_user_selector()
        #login_page.click_login_user_selector() # Кликнули по выпадающему списку
        login_page.should_be_login_user()
        login_page.click_login_user()  # Выбрали Гарри Поттера - user_name напрямую вписан в locators
        login_page.should_be_login_button()
        login_page.click_login_button()  # Кликнули по кнопке Login

        account_page = AccountPage(browser, browser.current_url)
        account_page.should_be_welcome()
        account_page.check_welcome_user(user_name)
        account_page.should_be_deposit_button()
        account_page.click_deposit_button()
        account_page.should_be_amount_field()
        account_page.write_to_deposit_field(amount)
        account_page.should_be_deposit_submit()
        account_page.click_deposit_submit()
        account_page.should_be_deposit_success_msg()
        account_page.check_deposit_success_msg_color('#FF0000') # RED COLOR!!!
        account_page.should_be_transactions_button()
        account_page.click_transactions_button()

        trans_page = TransPage(browser, browser.current_url)
        trans_page.should_be_trans_table()

        trans_page.should_be_trans_cell_date() # <<<<<<<<<< null table
        trans_page.check_trans_cell_date()
        trans_page.should_be_trans_cell_amount()
        trans_page.check_trans_cell_amount(amount)

        trans_page.should_be_logout_btn()
        trans_page.click_logout_btn()
