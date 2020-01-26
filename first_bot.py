import time
from selenium import webdriver

class ticket_buyer:

    def __init__(self, festival, ticket):
        self.festival = festival
        self.ticket = ticket
        self.driver = webdriver.Chrome(executable_path='C:/Users/niekb/Downloads/chromedriver_win32\chromedriver.exe')

    def ticket_finder(self):
        self.driver.get('http://www.ticketswap.nl/');
        time.sleep(1)
        search_box = self.driver.find_element_by_xpath("//input[@placeholder=\"Zoeken naar evenementen, locaties en steden\"]")
        time.sleep(1)
        search_box.send_keys(self.festival)
        time.sleep(2)
        festival_box = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/h4').click()
        time.sleep(1)
        ticket_box = self.driver.find_element_by_xpath(f'//h4[text()="{self.ticket}"]')
        self.driver.execute_script("arguments[0].click();", ticket_box)
        time.sleep(3)
        print('ticket found')
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/button').click()
        time.sleep(1)


    def find_available(self):
        result = True
        if self.driver.find_elements_by_xpath('//h2[text()="Op dit moment worden er geen tickets aangeboden"]'):
            result = False

        return result

    def refresher(self):
        self.driver.refresh()
        time.sleep(3)
        print('...finding ticket')

    def buyer(self):
        available_ticket = self.driver.find_element_by_xpath(f'//h3[contains(text(),"{self.ticket}")]')
        self.driver.execute_script("arguments[0].click();", available_ticket)
        time.sleep(1)
        clicker = self.driver.find_element_by_xpath('//button[text()="Koop een ticket"]')
        self.driver.execute_script("arguments[0].click();", clicker)
        time.sleep(5)
        return True

    def sign_in(self, email, password):
        clicker = self.driver.find_element_by_xpath('//button[text()="Koop een ticket"]')
        self.driver.execute_script("arguments[0].click();", clicker)
        time.sleep(2)
        main_page = self.driver.current_window_handle
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/button').click()
        time.sleep(1)
        for handle in self.driver.window_handles:
                if handle != main_page:
                        login_page = handle
        self.driver.switch_to.window(login_page)
        self.driver.find_element_by_xpath('//input[@id="email"]').send_keys(email)
        time.sleep(1)
        self.driver.find_element_by_xpath('//input[@id="pass"]').send_keys(password)
        time.sleep(1)
        login_button = self.driver.find_element_by_xpath('//input[@value="Log In"]')
        self.driver.execute_script("arguments[0].click();", login_button)
        self.driver.switch_to.window(main_page)
        time.sleep(5)
