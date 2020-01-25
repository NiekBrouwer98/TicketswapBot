import time
from selenium import webdriver

def sign_in(driver, email, password):
        driver.get('http://www.ticketswap.nl/');
        time.sleep(1)
        driver.find_element_by_xpath('//button[text()="Inloggen"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/button').click()

driver = webdriver.Chrome(executable_path='C:/Users/niekb/Downloads/chromedriver_win32\chromedriver.exe')
sign_in(driver, 'test@test.com', 'test123')
