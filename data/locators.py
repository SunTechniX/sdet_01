from selenium.webdriver.common.by import By


class AccountPageLocators:
    ACC_WELCOME_TEXT = (By.XPATH, "//strong[contains(text(),'Welcome')]")
    ACC_WELCOME_USER = (By.XPATH, "//strong[contains(text(),'Welcome')]/span")
    ACC_DEPOSIT_BTN = (By.XPATH, "//button[starts-with(text(),'Deposit')]")
    ACC_AMOUNT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
    ACC_DEPOSIT_SUBMIT = (By.XPATH, "//button[@type='submit']")
    ACC_DEPOSIT_SUCCESS_MSG = (By.XPATH, "//span[@ng-show='message']")
    ACC_TRANSACT_BTN = (By.XPATH, "//button[@ng-click='transactions()']")

class MainPageLocators:
    @staticmethod
    def base_button(name_btn: str) -> tuple[By, str]:
        '''
        Возвращает совокупный локатор в виде кортежа из метода поиска элемента и локатора элемента

        :param name_btn: название кнопки
        '''
        return By.XPATH, f"//button[starts-with(text(),'{name_btn}')]"

class LoginPageLocators:
    @staticmethod
    def login_user(user_name: str) -> tuple[By, str]:
        '''
        Возвращает совокупный локатор в виде кортежа из метода поиска элемента и локатора элемента

        :param user_name: имя пользователя
        '''
        return By.XPATH, f'//option[contains(text(),"{user_name}")]'

    LOGIN_CUSTOMER_BTN = (By.XPATH, "//button[starts-with(text(),'Customer')]")
    LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')

class TransPageLocators:
    @staticmethod
    def trans_table_cell(cell_id: int) -> tuple[By, str]:
        '''
        Возвращает совокупный локатор в виде кортежа из метода поиска элемента и локатора элемента

        :param cell_id: номер столбца
        '''
        return By.XPATH, f"//tbody/tr[contains(@id,'anchor')][last()]//td[{cell_id}]"
