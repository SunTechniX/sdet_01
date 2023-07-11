import locale
from datetime import datetime, date

from .main_page import MainPage
from data.locators import TransPageLocators
from data.account_data import AccountData

class TransPage(MainPage):
    def assert_trans_cell_amount(self) -> None:
        ''' Проверяет наличие ячейки 'Amount' в таблице Trnsactions '''
        assert self.is_element_present(TransPageLocators.trans_table_cell(2)), "Колонка 'Amount' в таблице отсутствует!"

    def assert_trans_cell_date(self) -> None:
        ''' Проверяет наличие ячейки 'Date' в таблице Trnsactions '''
        assert self.is_element_present(TransPageLocators.trans_table_cell(1)), "Колонка 'Date' в таблице отсутствует!"

    def compare_trans_cell_amount(self, amount: int) -> None:
        '''
        Сравнивает сумму снесения на депозит с суммой в таблице

        :param amount: сумма внесения на депозит (int)
        '''
        trans_amount = int(self.get_element_text(TransPageLocators.trans_table_cell(2)))
        assert amount == trans_amount, "Сумма перевода не соответвет ожидаемой!"

    def compare_trans_cell_date(self) -> None:
        ''' Сравнивает текущую дату с датой в таблице Transactions '''
        dtext = self.get_element_text(TransPageLocators.trans_table_cell(1))
        datenow = date.today().strftime("%b %d, %Y")
        assert datenow in dtext, "Текущая дата и дата транзакции не совпадают!"

    def transaction(self) -> None:
        ''' Проверяет таблицу Transactions на наличие записи о проведённой операции '''
        self.assert_trans_cell_date()
        self.compare_trans_cell_date()
        self.assert_trans_cell_amount()
        self.compare_trans_cell_amount(AccountData.AMOUNT)
