from password_encrypter import classified_information
from first_bot import ticket_buyer


def main_buyer():
    festival = input('Which festival would you like to go?\n')
    ticket = input('Which kind of ticket would you like to buy?\n')

    customer_choice = ticket_buyer(festival, ticket)

    customer_choice.ticket_finder()
    available = customer_choice.find_available()

    while available is False:
        customer_choice.refresher()

    if available is True:
        customer_choice.buyer()
        decrypt = classified_information('', 1, 'pw_file.txt')
        f = open('pw_file.txt', 'r')
        f1 = f.readlines()
        encrypted_email = f1[0]
        encrypted_password = f1[1]
        email = str(decrypt.decrypter(encrypted_email))
        password = str(decrypt.decrypter(encrypted_password))
        customer_choice.sign_in(email, password)

if __name__ == '__main__':
    decrypt = classified_information('', 1, 'pw_file.txt')
    decrypt.main_encrypter()
    main_buyer()
