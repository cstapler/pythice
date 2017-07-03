import codecs
from crypto import CryptoKit


def main():
    plaintext = bytes("Burning 'em, if you ain't quick and nimble\n \
                 I go crazy when I hear a cymbal", 'utf-8')
    key = bytes("ICE", "utf-8")
    xor_kit = CryptoKit()
    cipher_bytes = xor_kit.encrypt_rep_xor(plaintext, key)

    print(codecs.encode(cipher_bytes, 'hex').decode())


if __name__ == '__main__':
    main()
