import codecs
from crypto import CryptoKit


def main():
    x = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    xor_breaker = CryptoKit()
    result = xor_breaker.break_xor_cipher(bytes.fromhex(x))
    print(result[1].decode())


if __name__ == '__main__':
    main()
