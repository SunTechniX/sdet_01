from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from selene.common.helpers import to_by
from selene.core.locator import Locator
from selene import browser

from selene import be, have, query
# from selene.support.shared import browser


class BasePageSS:

    # def __init__(self, browser):
    #     self.browser = browser

    def find_element(self, css_or_xpath_or_by: str) -> WebElement:
        by = to_by(css_or_xpath_or_by)
        return browser.driver.find_element(*by)

    def is_element_present(self, locator: tuple[By, str], timeout: int = 10) -> bool:
        ''' Проверяет наличие WebElement-а с ожиданием в timeout секунд '''
        element = browser.element(locator[1])
        try:
            # WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
            element.should(be.present).with_(timeout=timeout)
        except TimeoutException:
            return False
        return True

    def click_to_element(self, locator: tuple[By, str], timeout: int = 10) -> None:
        '''
        Ожидает появления кликабельности элемента и кликает на него

        :param locator: Кортеж из метода поиска элемента и локатора элемента
        :param timeout: Время ожидания элемента в секундах
        '''
        # WebDriverWait(self.browser, timeout).until(EC.element_to_be_clickable(locator)).click()
        element = browser.element(locator[1])
        element.should(be.clickable)
        element.click()

    def compare_element_text(self, locator: tuple[By, str], text: str, timeout: int = 10):
        element = browser.element(locator[1])
        assert text == element.should(be.present).with_(timeout=timeout).text,\
            f"{text} не соответствует ожидаемому!"

    def get_element(self, locator: tuple, timeout: int = 10) -> WebElement:
        ''' Ожидает появление WebElement-а и возвращает его '''
        # return WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator))
        return browser.element(locator[1])

    def get_element_text(self, locator: tuple[By, str]) -> str:
        ''' Возвращает текст написанный на WebElement-е '''
        ## return self.get_element(locator).text
        element = browser.element(locator[1])
        return element.get(query.text)


    def write_to_element(self, locator: tuple[By, str], text: str, timeout=10) -> None:
        ''' Ожидает появления WebElement-а и пишет в него text '''
        # WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(locator)).send_keys(text)
        element = browser.element(locator[1])
        element.should(be.present).with_(timeout=timeout).send_keys(text)

    def reload_page(self):
        browser.refresh()
