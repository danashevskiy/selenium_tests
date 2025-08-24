from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

PAGE = 'http://priority.finwhale.ru'
INN = "7708737490"
NAME = "Иван"
SURENAME = "Иванович"
SEC_NAME = "Иванов"
PHONE = "89216362048"
EMAIL = "danashevskiy@gmail.com"
PAGE_TITLE = 'FINWHALE PRIORITY'


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
