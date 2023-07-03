import pytest

from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.trans_page import TransPage


@pytest.mark.harry_potter
class TestHarryPotter:
    def test_harry_potter(self, browser):
        browser.delete_all_cookies()
        login_page = LoginPage(browser)
        login_page.login_procedure()
        account_page = AccountPage(browser)
        account_page.account_procedure()
        trans_page = TransPage(browser)
        trans_page.verify_transaction()
        trans_page.click_logout_btn()
        trans_page.click_home_btn()

