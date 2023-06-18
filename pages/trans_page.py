from .base_page import BasePage
from .locators import TransPageLocators
from datetime import datetime
import locale


class TransPage(BasePage):
    def click_login_button(self):
        self.browser.find_element(*TransPageLocators.TRANS_TABLE).click()

    def check_trans_cell_amount(self, amount):
        trans_amount_s = self.browser.find_element(*TransPageLocators.TRANS_CELL_AMOUNT).text
        trans_amount = -1
        if trans_amount_s.isnumeric():
            trans_amount = int(trans_amount_s)
        assert amount == trans_amount, "Transaction Amount is not Equal!"

    def check_trans_cell_date(self):
        locale.setlocale(locale.LC_TIME, 'en')
        dtext = self.browser.find_element(*TransPageLocators.TRANS_CELL_DATE).text # Jun 17, 2023 7:50:09 AM
        month = datetime.now().strftime("%b")
        year = str(datetime.now().year)
        day = str(datetime.now().day)
        assert day in dtext and month in dtext and year in dtext, "Transaction Date is not Equal!"


    def should_be_trans_table(self):
        assert self.is_element_present(*TransPageLocators.TRANS_TABLE), "Transactions Table is not presented"

    def should_be_trans_cell_amount(self):
        assert self.is_element_present(*TransPageLocators.TRANS_CELL_AMOUNT), "Trans Cell Amount is not presented"

    def should_be_trans_cell_date(self):
        assert self.is_element_present(*TransPageLocators.TRANS_CELL_DATE), "Trans Cell Date is not presented"
