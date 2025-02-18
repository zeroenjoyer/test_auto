from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url) для первого варианта перехода на новую вкладку
        # alert = self.browser.switch_to.alert # если разраб даст ёбу и сделает после нажатия на кнопку алерт, то может крашнуться много тестов, поэтому одной строчкой можно это пофиксить - эт плюс патерна page object, чтобы не добавлять эту строчку во все тесты
        # alert.accept()
    
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented" #Обратите внимание здесь на символ *, он указывает на то, что мы передали именно пару, и этот кортеж нужно распаковать.
        