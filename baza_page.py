from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from driver import Driver


class FinhwalePriorityPage:
    '''
    Page Class to create test cases for finwhale priority page
    '''
    def __init__(self):
        pass
        
    def accept_cookies(self):
        button = Driver().find_element(By.XPATH, "//button[.//p[text()='Принять']]")
        button.click()
        
    def login(self):
        login_button = Driver().find_element(by=By.CSS_SELECTOR, value="button")
        login_button.click()
        
    def register_user(self):
        button = Driver().find_element(By.XPATH, "//button[.//p[text()='Зарегистрироваться']]")
        Driver().execute_script("arguments[0].click();", button)
        return FinwhaleRegistrationForm()
        
class FinwhaleRegistrationForm:
    '''
    Component class for registration form filling
    '''
    def __init__(self):
        pass
    
    def choose_organization(self, num):
        inn = Driver().find_element(By.ID, "company_inn")
        inn.send_keys(num)
        dropdown = WebDriverWait(Driver(), 10).until(  
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "input-search__options")) 
        )
        option = WebDriverWait(Driver(), 10).until( 
            EC.element_to_be_clickable((By.XPATH, "//li[@class='input-search__option'][1]")) 
        )
        option.click()
        
    
    def set_same_address(self):
        check_adr = Driver().find_element(By.CLASS_NAME, "checkbox__point")
        check_adr.click()
    
    
    def choose_segment(self):
        segment = Driver().find_element(By.ID, "segment")
        segment.click()
        dropdown = WebDriverWait(Driver(), 10).until(   
            EC.visibility_of_element_located((By.CLASS_NAME, "select__option"))
        )
        option = WebDriverWait(Driver(), 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='select__result'][1]"))
        )
        option.click()
    
    
    def fill_surname(self, name):
        surename = Driver().find_element(By.ID,"last_name")
        surename.send_keys(name) 
        
    
    def fill_name(self, name):
        Driver().find_element(By.ID, "first_name").send_keys(name)
        
    def fill_sec_name(self, name):
        Driver().find_element(By.ID, "sur_name").send_keys(name)
    
    def fill_phone_number(self, num):
        phone = Driver().find_element(By.ID,"phone") 
        phone.send_keys(num)
        
    
    def fill_email(self, email):
        mail = Driver().find_element(By.ID, "email")
        mail.send_keys(email)
        
    
    def choose_curator(self):
        dist = Driver().find_element(By.ID, "curator")
        Driver().execute_script("arguments[0].scrollIntoView(true);", dist)
        dist.click()
        dropdown = WebDriverWait(Driver(), 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME,"select__options.select__options_certificate"))
        )
        option = WebDriverWait(Driver(), 10).until( 
            EC.presence_of_element_located((By.XPATH, "//span[@class='select__result'][1]")) 
        )
        option = Driver().find_elements(By.XPATH, "//span[@class='select__result']")
        option[5].click()
        
     
    def set_wo_manager(self):
        manager_check = Driver().find_element(By.ID, "agreementMember")
        Driver().execute_script("arguments[0].click();", manager_check)
         
     
    def set_notification_email(self):
        notify = Driver().find_element(By.ID,"dataAgreement")
        Driver().execute_script("arguments[0].click();", notify)
         
     
    def set_privacy(self):
        privacy = Driver().find_element(By.ID, "privacy")
        Driver().execute_script("arguments[0].click();", privacy)
         
     
    def send_registration_form(self):
        button = Driver().find_element(By.CLASS_NAME, "tab-modal__content_button.tab-modal__content_button_center")
        button.click()

