import pytest

from data.account_data import AccountData
from data.login_data import LoginData
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.trans_page import TransPage


@pytest.mark.harry_potter
class TestHarryPotter:
    def test_harry_potter(self, browser, browser_del_cookie):
        login_page = LoginPage(browser)
        login_page.login()
        account_page = AccountPage(browser)
        account_page.compare_welcome_user(LoginData.USER)
        account_page.click_btn_name('deposit()')
        account_page.write_to_deposit_field(AccountData.AMOUNT)
        account_page.click_btn_deposit_submit()
        account_page.compare_deposit_success_msg_color(AccountData.COLOR)
        account_page.click_btn_name('transactions()')
        trans_page = TransPage(browser)
        trans_page.transaction()
        trans_page.click_btn_starts_with('Logout')
        trans_page.click_btn_starts_with('Home')

