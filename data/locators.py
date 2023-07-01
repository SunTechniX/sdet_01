from selenium.webdriver.common.by import By


class AccountPageLocators():
    ACC_WELCOME_TEXT = (By.XPATH, "//strong[contains(text(),'Welcome')]")
    ACC_WELCOME_USER = (By.XPATH, "//strong[contains(text(),'Welcome')]/span")
    ACC_DEPOSIT_BTN = (By.XPATH, "//button[starts-with(text(),'Deposit')]")
    ACC_AMOUNT_FIELD = (By.XPATH, "//input[@ng-model='amount']")
    ACC_DEPOSIT_SUBMIT = (By.XPATH, "//button[@type='submit']")
    ACC_DEPOSIT_SUCCESS_MSG = (By.XPATH, "//span[@ng-show='message']")
    ACC_TRANSACT_BTN = (By.XPATH, "//button[@ng-click='transactions()']")

class MainPageLocators():
    @staticmethod
    def base_button(name_btn: str) -> tuple[By, str]:
        '''
        Вернуть совокупный локатор в виде кортежа из метода поиска элемента (By) и локатора элемента (str)

        :param name_btn: название кнопки (int)
        '''
        return By.XPATH, f"//button[starts-with(text(),'{name_btn}')]"

class LoginPageLocators():
    LOGIN_CUSTOMER_BTN = (By.XPATH, "//button[starts-with(text(),'Customer')]")
    LOGIN_USER_SELECT = (By.ID, '#userSelect')
    LOGIN_USER = (By.XPATH, '//option[contains(text(),"Harry Potter")]') # make param for user_name?
    LOGIN_BTN = (By.XPATH, '//button[@type="submit"]')

class TransPageLocators():
    TRANS_TABLE = (By.CSS_SELECTOR, '.table-striped')
    TRANS_CELL_DATE = (By.XPATH, "//tbody/tr[contains(@id,'anchor')][last()]//td[1]")
    TRANS_CELL_AMOUNT = (By.XPATH, "//tbody/tr[contains(@id,'anchor')][last()]//td[2]")

