import codecs
from crypto import CryptoKit

xor_kit = CryptoKit()


def test():
    in_1 = bytes('this is a test', 'utf-8')
    in_2 = bytes('wokka wokka!!!', 'utf-8')
    distance = xor_kit.hamming_distance(in_1, in_2)
    assert(distance == 37)


def main():
    with open('inputs1c6.txt', 'r') as in_file:
        text_bytes = codecs.decode(in_file.read().replace("\n", ""), 'base64')
        print(text)
        for key_size in range(39, 40):
            text1 = text[:key_size]
            text2 = text[key_size: key_size*2]
            print(text1)
            print(text2)
            print(xor_kit.hamming_distance(text1, text2))


if __name__ == '__main__':
    test()
    main()
