class classified_information:

    def __init__(self, information, number, file):
        self.information = information
        self.i = number
        self.file = file
        self.encrypted_str = ''

    def encrypter(self):
        # encrypted_str = ''
        for j in self.information[::-(self.i)]:
            self.encrypted_str += chr(ord(j)+1)

        return self.encrypted_str

    def decrypter(self, encrypted_str):
        decrypted_string = ''
        for j in encrypted_str[::-(self.i)]:
            decrypted_string += chr(ord(j)-1)

        return decrypted_string

    def write_to_txt_file(self):
        f = open(self.file, 'a')
        f.write(f'{self.encrypted_str}\n')
        print('encryption complete')

    def main_encrypter(self):
        print('All your personal information will be processed in an encrypted form.\n')
        email = input('What is your emailadres?\n')
        pw = input('What is your password?\n')

        fb_email = classified_information(email, 1, 'pw_file.txt')
        fb_pw = classified_information(pw, 1, 'pw_file.txt')

        print(f'This is your encrypted email: {fb_email.encrypter()}')
        print(f'This is your encrypted password: {fb_pw.encrypter()}')
        fb_email.write_to_txt_file()
        fb_pw.write_to_txt_file()

    def cleaning(self):
        open(self.file, 'w').close()


#test erasing file
erase_file = classified_information('test string', 1, 'pw_file.txt')
erase_file.cleaning()
