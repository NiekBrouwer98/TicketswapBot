import time
from selenium import webdriver

def sign_in(driver, email, password):
        driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/button').click()
        time.sleep(1)
        for handle in driver.window_handles:
                if handle != main_page:
                        login_page = handle
        driver.switch_to.window(login_page)
        driver.find_element_by_xpath('//input[@name=\"email\"]').send_keys(email)
        time.sleep(1)
        driver.find_element_by_xpath('//input[@name=\"pass\"]').send_keys(password)
        time.sleep(1)
        driver.find_element_by_xpath('//button[@name=\"login\"]').click()
        driver.switch_to.window(main_page)
        time.sleep(5)

driver = webdriver.Chrome(executable_path='C:/Users/niekb/Downloads/chromedriver_win32\chromedriver.exe')
with open('pw_file.txt', 'r') as f:
        line = f.readlines()
        email = str(line[0])
        pw = str(line[1])

sign_in(driver, email, pw)


