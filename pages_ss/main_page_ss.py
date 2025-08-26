from .base_page_ss import BasePageSS
from data.locators import MainPageLocators


class MainPageSS(BasePageSS):

    # def __init__(self, browser):
    #     super(MainPageSS, self).__init__(browser)

    def click_btn_starts_with(self, name_btn: str) -> None:
        '''
        Нажимает на кнопку name_btn

        :param name_btn: название кнопки
        '''
        self.click_to_element(MainPageLocators.button_starts_with(name_btn))
