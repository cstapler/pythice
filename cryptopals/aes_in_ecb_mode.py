import codecs
from Cryptodome.Cipher import AES


def main():
    key = b"YELLOW SUBMARINE"
    cipher = AES.new(key, AES.MODE_ECB)
    with open('input_s1c7.txt', 'rb') as in_file:
        text_bytes = codecs.decode(in_file.read(), 'base64')
        print(cipher.decrypt(text_bytes))



if __name__ == '__main__':
    main()
