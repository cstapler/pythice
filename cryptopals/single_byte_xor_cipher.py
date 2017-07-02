import codecs
from crypto import CryptoKit


def main():
    x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    xor_breaker = CryptoKit()
    plain_text = xor_breaker.break_xor_cipher(x)
    print(plain_text)


if __name__ == '__main__':
    main()
