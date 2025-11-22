import pytest
import baza_page
from driver import Driver

PAGE = 'http://priority.finwhale.ru'
INN = "7708737490"
NAME = "Иван"
SURENAME = "Иванович"
SEC_NAME = "Иванов"
PHONE = "89216362011"
EMAIL = "danashevskii@gmail.com"
PAGE_TITLE = 'FINWHALE PRIORITY'

@pytest.fixture(scope='class', autouse=True)
def resource_page():
    '''fixture: Обертка для тестового класса'''
    #print('>>', 'fixture: Запуск обертки для тестовго класса')
    browser = Driver()
    browser.get(PAGE)
    finwhale = baza_page.FinhwalePriorityPage()
    yield finwhale
    browser.close()
    #print('>>', 'fixture: Завершение обертки для тестовго класса')
    

#def test_browse(resource_page):
    #finwhale = baza_page.FinhwalePriorityPage('http://priority.finwhale.ru')
    #data = f_wrapper_class()
#    'FINWHALE PRIORITY' in resource_page._driver.title
    #assert True
    
def test_registration(resource_page):
    resource_page.accept_cookies()
    resource_page.login()
    user_reg = resource_page.register_user()
    assert "Регистрация" in Driver().page_source
    user_reg.choose_organization(INN)
    user_reg.set_same_address()
    user_reg.choose_segment()
    user_reg.fill_name(NAME)
    user_reg.fill_surname(SURENAME)
    user_reg.fill_sec_name(SEC_NAME)
    user_reg.fill_phone_number(PHONE)
    user_reg.fill_email(EMAIL)
    user_reg.choose_curator()
    user_reg.set_wo_manager()
    user_reg.set_notification_email()
    user_reg.set_privacy()
    user_reg.send_registration_form()
    assert "Введите код подтверждения" in Driver().page_source
    

