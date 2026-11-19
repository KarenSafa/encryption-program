from string import ascii_letters, digits, punctuation
lazy from random import shuffle
from os.path import exists
from os import stat

encryption_content = ascii_letters + digits + punctuation

def check_file(file_path='encryption key') -> bool:
    if not(exists(file_path)) or stat(file_path).st_size == 0:
        return False
    return True

def create_file(encryption_content=encryption_content, file_path='encryption key'):
    encryption_content = list(encryption_content)
    encryption_key = encryption_content.copy()
    shuffle(encryption_key)
    encryption_key = '\n'.join(encryption_key)
    with open(file_path, 'w') as file:
        file.write(encryption_key)

def read_file(file_path='encryption key'):
    with open(file_path, 'r') as file:
        return file.read()

def encrypt(encryption_content=encryption_content) -> str:
    encryption_key = read_file()
    encryption_key = encryption_key.split('\n')
    text = input('Enter a text to encrypt: ')
    cipher_text = ''
    for i in text:
        index = encryption_content.index(i)
        cipher_text += encryption_key[index]
    return cipher_text

def decrypt(encryption_content=encryption_content) -> str:
    encryption_key = read_file()
    encryption_key = encryption_key.split('\n')
    encrypted_text = input('Enter a text to decrypt: ')
    decrypted_text = ''
    for i in encrypted_text:
        index = encryption_key.index(i)
        decrypted_text += encryption_content[index]
    return decrypted_text

def main():
    while True:
        print('''1.Encryption
2.Decryption
3.re-encryption key
4.Exit''')
        print('-------------------------------')
        while True:
            try:
                option = int(input('Enter what you need: '))
                break
            except ValueError:
                print('-------------------------------')
                print('Enter the number of the options')
        print('-------------------------------')

        if option == 1:
            if check_file():
                print(encrypt())
                print('-------------------------------')
            else:
                create_file()
                print(encrypt())
                print('-------------------------------')

        elif option == 2:
            if check_file():
                print(decrypt())
                print('-------------------------------')
            else:
                create_file()
                print(decrypt())
                print('-------------------------------')

        elif option == 3:
            create_file()

        elif option == 4:
            break

        else:
            print('Invalid option')
            

if __name__ == '__main__':
    main()