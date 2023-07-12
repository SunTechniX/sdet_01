import locale
from datetime import datetime, date

from .main_page import MainPage
from data.locators import TransPageLocators
from data.account_data import AccountData

class TransPage(MainPage):
    def assert_trans_cell_amount_exist(self) -> None:
        ''' Проверяет наличие ячейки 'Amount' в таблице Trnsactions '''
        assert self.is_element_present(TransPageLocators.trans_table_cell(2)), "Колонка 'Amount' в таблице отсутствует!"

    def assert_trans_cell_date_exist(self) -> None:
        ''' Проверяет наличие ячейки 'Date' в таблице Trnsactions '''
        assert self.is_element_present(TransPageLocators.trans_table_cell(1)), "Колонка 'Date' в таблице отсутствует!"

    def assert_trans_cell_amount_compare(self, amount: int) -> None:
        '''
        Сравнивает сумму снесения на депозит с суммой в таблице

        :param amount: сумма внесения на депозит (int)
        '''
        trans_amount = int(self.get_element_text(TransPageLocators.trans_table_cell(2)))
        assert amount == trans_amount, "Сумма перевода не соответвет ожидаемой!"

    def assert_trans_cell_date_compare(self) -> None:
        ''' Сравнивает текущую дату с датой в таблице Transactions '''
        date_in_table = self.get_element_text(TransPageLocators.trans_table_cell(1))
        today_date = date.today().strftime("%b %d, %Y")
        assert today_date in date_in_table, "Текущая дата и дата транзакции не совпадают!"

    def assert_transaction(self) -> None:
        ''' Проверяет таблицу Transactions на наличие записи о проведённой операции '''
        self.assert_trans_cell_date_exist()
        self.assert_trans_cell_date_compare()
        self.assert_trans_cell_amount_exist()
        self.assert_trans_cell_amount_compare(AccountData.AMOUNT)
