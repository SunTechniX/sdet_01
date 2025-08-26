import pytest

from data.account_data import AccountData
from data.login_data import LoginData
# from pages.home_page import HomePage
from pages_ss.login_page_ss import LoginPageSS
from pages_ss.account_page_ss import AccountPageSS
# from pages.trans_page import TransPage


@pytest.mark.harry_potter
class TestHarryPotterSS:

    def test_harry_potter_ss(self, browser_selene, selene_del_cookie):
        login_page = LoginPageSS()
        login_page.make_login()
        account_page = AccountPageSS()
        account_page.compare_welcome_user(LoginData.USER)
        account_page.click_btn_name('deposit()')
        account_page.write_to_deposit_field(AccountData.AMOUNT)
        account_page.click_btn_deposit_submit()
        account_page.compare_deposit_success_msg_color(AccountData.COLOR)
        account_page.click_btn_name('transactions()')
        # trans_page = TransPage()
        # trans_page.assert_transaction()
        # trans_page.click_btn_starts_with('Logout')
        # trans_page.click_btn_starts_with('Home')
        # home_page = HomePage()
        # home_page.assert_home_page()

