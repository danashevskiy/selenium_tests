import pytest
import baza_page

FINWHALE_PAGE = 'http://priority.finwhale.ru'

@pytest.fixture(scope='class', autouse=True)
def my_resource_instance():
    '''fixture: Обертка для тестового класса'''
    print('>>', 'fixture: Запуск обертки для тестовго класса')
    finwhale = baza_page.FinhwalePriorityPage(FINWHALE_PAGE)
    yield finwhale
    finwhale.close_page()
    print('>>', 'fixture: Завершение обертки для тестовго класса')
    

def test_browse(my_resource_instance):
    #finwhale = baza_page.FinhwalePriorityPage('http://priority.finwhale.ru')
    #data = f_wrapper_class()
    'FINWHALE PRIORITY' in my_resource_instance._driver.title
    #assert True
    

