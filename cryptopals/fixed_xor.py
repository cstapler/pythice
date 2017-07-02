import codecs
from crypto import CryptoKit


def main():
    hex_1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    hex_2 = bytes.fromhex('686974207468652062756c6c277320657965')

    xor_breaker = CryptoKit()
    result = xor_breaker.hex_xor(hex_1, hex_2)
    print(codecs.encode(result, 'hex').decode())


if __name__ == '__main__':
    main()
