import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ticket_buyer:

    def __init__(self, festival, ticket):
        self.festival = festival
        self.ticket = ticket
        self.driver = webdriver.Chrome(executable_path='C:/Users/niekb/Downloads/chromedriver_win32\chromedriver.exe')

    def ticket_finder(self):
        self.driver.get('http://www.ticketswap.nl/');
        time.sleep(1) # Let the user actually see something!
        search_box = self.driver.find_element_by_xpath("//input[@placeholder=\"Zoeken naar evenementen, locaties en steden\"]")
        time.sleep(1)
        search_box.send_keys(self.festival)
        time.sleep(5)
        festival_box = self.driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[2]/div/div[2]/div[2]/div/h4').click()
        time.sleep(5)
        ticket_box = self.driver.find_element_by_xpath(f'//h4[text()="{self.ticket}"]')
        self.driver.execute_script("arguments[0].click();", ticket_box)
        print('ticket found')

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
        print('Ticket available!')


def main():
    festival = input('Which festival would you like to go?\n')
    ticket = input('Which kind of ticket would you like to buy?\n')

    customer_choice = ticket_buyer(festival, ticket)

    customer_choice.ticket_finder()
    available = customer_choice.find_available()

    if available is True:
         customer_choice.buyer()
    if available is False:
        while customer_choice.find_available() is False:
            customer_choice.refresher()

        if customer_choice.find_available() is True:
            customer_choice.buyer()

main()
