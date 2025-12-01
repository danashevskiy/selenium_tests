import pytest
import baza_page
from driver import Driver
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By
from playwright.sync_api import Page, expect, Browser, BrowserContext
import re
#import asyncio

PAGE = 'http://priority.finwhale.ru'
INN = "7708737490"
NAME = "Иван"
SURENAME = "Иванович"
SEC_NAME = "Иванов"
PHONE = "+79216362048"
EMAIL = "danashevskii@yandex.ru"
PAGE_TITLE = 'FINWHALE PRIORITY'
PASSWORD = 'Danashevskiy!'

@pytest.fixture(scope='function', autouse=True)
def resource_page(page: Page):
    '''fixture: Обертка для тестового класса'''
    browser = Driver(page)
    browser.goto('http://priority.finwhale.ru')
    finwhale = baza_page.FinhwalePriorityPage()
    yield finwhale
    Driver.reset_instances()

def browse(resource_page, page: Page):
    page.goto('http://priority.finwhale.ru')
    expect(page).to_have_title(re.compile(PAGE_TITLE))
    
def registration(resource_page):
    resource_page.accept_cookies()
    #resource_page.login()
    #user_reg = resource_page.register_user()
    #assert "Регистрация" in Driver().page_source
    #user_reg.choose_organization(INN)
    #user_reg.set_same_address()
    #user_reg.choose_segment()
    #user_reg.fill_name(NAME)
    #user_reg.fill_surname(SURENAME)
    #user_reg.fill_sec_name(SEC_NAME)
    #user_reg.fill_phone_number(PHONE)
    #user_reg.fill_email(EMAIL)
    #user_reg.choose_curator()
    #user_reg.set_wo_manager()
    #user_reg.set_notification_email()
    #user_reg.set_privacy()
    #user_reg.send_registration_form()
    #assert "Введите код подтверждения" in Driver().page_source


@pytest.mark.parametrize("login, pswd, xpath, text", [
    (PHONE, PASSWORD, "div.title.title_black.title_upper", "Профиль"),
    (PHONE, SURENAME, "div.modal__wrapper", "Неверный логин или пароль")
], ids=["Correct login", "Incorrect password"])    
def test_login(resource_page, login, pswd, xpath, text):
    resource_page.open_menu()
    user_login = resource_page.login()
    user_login.type_login(login)
    user_login.type_password(pswd)
    user_login.press_login()
    expect(Driver().locator(xpath)).to_contain_text(text)

