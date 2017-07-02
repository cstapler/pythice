#!/usr/bin/env python

import codecs

def xor_hex(hex_one, hex_two):
    dec_one = codecs.decode(hex_one, 'hex')
    dec_two = codecs.decode(hex_two, 'hex')
    for x in len(dec_one):


def main():
    hex_input = input()
    hex_second = input()
    result = xor_hex(hex_input, hex_second)
    print(result)


if __name__ == "__main__":
    main()
