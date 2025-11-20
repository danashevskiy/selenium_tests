from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FinhwalePriorityPage:
    '''
    Page Class to create test cases for finwhale priority page
    '''
    _driver = None
    _wait = None
    
    def __init__(self, page):
        self._driver = webdriver.Firefox()
        self._wait = WebDriverWait(self._driver, 10)
        self._driver.get(page)
        
    def close_page(self):
        self._driver.close()
        
    def accept_cookies(self):
        button = self._driver.find_element(By.XPATH, "//button[.//p[text()='Принять']]")
        button.click()
        
    def login(self):
        login_button = self._driver.find_element(by=By.CSS_SELECTOR, value="button")
        login_button.click()
        
    def register_user(self):
        button = self._driver.find_element(By.XPATH, "//button[.//p[text()='Зарегистрироваться']]")
        self._driver.execute_script("arguments[0].click();", button)
        return FinwhaleRegistrationForm(self._driver, self._wait)
        
class FinwhaleRegistrationForm:
    '''
    Component class for registration form filling
    '''
    _driver = None
    _wait = None
    
    def __init__(self, driver, wait):
        self._driver = driver
        self._wait = wait
    
    def choose_organization(self, num):
        inn = self._driver.find_element(By.ID, "company_inn")
        inn.send_keys(num)
        dropdown = self._wait.until(  
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "input-search__options")) 
        )
        option = self._wait.until( 
            EC.element_to_be_clickable((By.XPATH, "//li[@class='input-search__option'][1]")) 
        )
        option.click()
        
    
    def set_same_address(self):
        check_adr = self._driver.find_element(By.CLASS_NAME, "checkbox__point")
        check_adr.click()
    
    
    def choose_segment(self):
        segment = self._driver.find_element(By.ID, "segment")
        segment.click()
        dropdown = self._wait.until(   
            EC.visibility_of_element_located((By.CLASS_NAME, "select__option"))
        )
        option = self._wait.until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='select__result'][1]"))
        )
        option.click()
    
    
    def fill_surname(self, name):
        surename = self._driver.find_element(By.ID,"last_name")
        surename.send_keys(name) 
        
    
    def fill_name(self, name):
        self._driver.find_element(By.ID, "first_name").send_keys(name)
        
    def fill_sec_name(self, name):
        self._driver.find_element(By.ID, "sur_name").send_keys(name)
    
    def fill_phone_number(self, num):
        phone = self._driver.find_element(By.ID,"phone") 
        phone.send_keys(num)
        
    
    def fill_email(self, email):
        mail = self._driver.find_element(By.ID, "email")
        mail.send_keys(email)
        
    
    def choose_curator(self):
        dist = self._driver.find_element(By.ID, "curator")
        self._driver.execute_script("arguments[0].scrollIntoView(true);", dist)
        dist.click()
        dropdown = self._wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME,"select__options.select__options_certificate"))
        )
        option = self._wait.until( 
            EC.presence_of_element_located((By.XPATH, "//span[@class='select__result'][1]")) 
        )
        option = self._driver.find_elements(By.XPATH, "//span[@class='select__result']")
        option[5].click()
        
     
    def set_wo_manager(self):
        manager_check = self._driver.find_element(By.ID, "agreementMember")
        self._driver.execute_script("arguments[0].click();", manager_check)
         
     
    def set_notification_email(self):
        notify = self._driver.find_element(By.ID,"dataAgreement")
        self._driver.execute_script("arguments[0].click();", notify)
         
     
    def set_privacy(self):
        privacy = self._driver.find_element(By.ID, "privacy")
        self._driver.execute_script("arguments[0].click();", privacy)
         
     
    def send_registration_form(self):
        button = self._driver.find_element(By.CLASS_NAME, "tab-modal__content_button.tab-modal__content_button_center")
        button.click()
    
'''
def page_browse(driver, wait):
    driver.get(PAGE)
    assert PAGE_TITLE in driver.title 

def accept_cookies(driver, wait):
    button = driver.find_element(By.XPATH, "//button[.//p[text()='Принять']]")
    button.click()
    
def init_registration(driver, wait):
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    login_button.click()
    assert "Авторизация" in driver.page_source
    button = driver.find_element(By.XPATH, "//button[.//p[text()='Зарегистрироваться']]")
    driver.execute_script("arguments[0].click();", button)
    assert "Регистрация" in driver.page_source

def fill_registration_form(driver, wait):
    inn = driver.find_element(By.ID, "company_inn")
    inn.send_keys(INN)
    dropdown = wait.until(  
        EC.visibility_of_all_elements_located((By.CLASS_NAME, "input-search__options")) 
    )
    option = wait.until( 
        EC.element_to_be_clickable((By.XPATH, "//li[@class='input-search__option'][1]")) 
    )
    option.click()
    check_adr = driver.find_element(By.CLASS_NAME, "checkbox__point")
    check_adr.click()
    segment = driver.find_element(By.ID, "segment")
    segment.click()
    dropdown = wait.until(   
        EC.visibility_of_element_located((By.CLASS_NAME, "select__option"))
    )
    option = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='select__result'][1]"))
    )
    option.click()
    surename = driver.find_element(By.ID,"last_name")
    surename.send_keys(SEC_NAME)
    name = driver.find_element(By.ID, "first_name")
    name.send_keys(NAME)
    sec_name = driver.find_element(By.ID, "sur_name") 
    sec_name.send_keys(SURENAME)
    phone = driver.find_element(By.ID,"phone") 
    phone.send_keys(PHONE)
    mail = driver.find_element(By.ID, "email")
    mail.send_keys(EMAIL)
    dist = driver.find_element(By.ID, "curator")
    driver.execute_script("arguments[0].scrollIntoView(true);", dist)
    dist.click()
    dropdown = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,"select__options.select__options_certificate"))
    )
    option = wait.until( 
        EC.presence_of_element_located((By.XPATH, "//span[@class='select__result'][1]")) 
    )
    option = driver.find_elements(By.XPATH, "//span[@class='select__result']")
    option[5].click()
    manager_check = driver.find_element(By.ID, "agreementMember")
    driver.execute_script("arguments[0].click();", manager_check)
    notify = driver.find_element(By.ID,"notificationMember")
    driver.execute_script("arguments[0].click();", notify)
    privacy = driver.find_element(By.ID, "privacy")
    driver.execute_script("arguments[0].click();", privacy)
    
def send_registration(driver, wait):
    button = driver.find_element(By.CLASS_NAME, "tab-modal__content_button.tab-modal__content_button_center")
    button.click()
    assert "Введите код подтверждения" in driver.page_source

def main():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    page_browse(driver, wait)
    accept_cookies(driver, wait)
    init_registration(driver, wait)
    fill_registration_form(driver, wait)
    send_registration(driver, wait)
    #driver.close()

main()
'''
