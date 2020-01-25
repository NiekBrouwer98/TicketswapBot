from password_encrypter import classified_information
from first_bot import ticket_buyer
from automated_sign_in import sign_in


def main():
    festival = input('Which festival would you like to go?\n')
    ticket = input('Which kind of ticket would you like to buy?\n')

    customer_choice = ticket_buyer(festival, ticket)

    customer_choice.ticket_finder()
    available = customer_choice.find_available()

    while available is False:
        customer_choice.refresher()

    if available is True:
        customer_choice.buyer()
        f = open('pw_file.txt', 'r')
        f1 = f.readlines()
        encrypted_email = f1[0]
        encrypted_password = f1[1]
        email = classified_information.decrypter(encrypted_email)
        password = classified_information.decrypter(encrypted_password)
        sign_in(email, password)

