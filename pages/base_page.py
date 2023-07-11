from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def is_element_present(self, locator: tuple[By, str], timeout: int = 10) -> bool:
        ''' Проверяет наличие WebElement-а с ожиданием в timeout секунд '''
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def click_to_element(self, locator: tuple[By, str], timeout: int = 10) -> None:
        '''
        Ожидает появления кликабельности элемента и кликает на него

        :param locator: Кортеж из метода поиска элемента и локатора элемента
        :param timeout: Время ожидания элемента в секундах
        '''
        WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()

    def compare_element_text(self, locator: tuple[By, str], text: str, timeout: int = 10):
        assert text == WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator)).text,\
            f"{text} не соответстует ожидаемому!"

    def get_element(self, locator: tuple, timeout: int = 10) -> WebElement:
        ''' Ожидает появление WebElement-а и возвращяет его '''
        return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))

    def get_element_text(self, locator: tuple[By, str]) -> str:
        ''' Возвращает текст написанный на WebElement-е '''
        return self.get_element(locator).text

    def write_to_element(self, locator: tuple[By, str], text: str, timeout=10) -> None:
        ''' Ожидает появления WebElement-а и пишет в него text '''
        WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator)).send_keys(text)
