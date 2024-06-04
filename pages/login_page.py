import PageObject_Selenium_Python.pages.locators
from PageObject_Selenium_Python.pages.base_page import BasePage
from PageObject_Selenium_Python.pages.locators import LoginPageLocators
from PageObject_Selenium_Python.pages.locators import MainPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.should_be_login_url(browser)
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, browser):
            # проверка на корректный url адрес (подстрока "login" есть в текущем url браузера)
        assert "login" in browser.current_url,  "Не корректный url адрес"

    def should_be_login_form(self):
            # проверка, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
            # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"