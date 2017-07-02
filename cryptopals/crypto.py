import codecs
from bitstring import BitArray

ENGLISH_CHAR_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835,
    'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610, 'h': 0.0492888,
    'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490,
    'm': 0.0202124, 'n': 0.0564513, 'o': 0.0596302, 'p': 0.0137645,
    'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357,
    'u': 0.0225134, 'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692,
    'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
}


class CryptoKit(object):
    """Cryptography Tools"""

    def __init__(self):
        super(CryptoKit, self).__init__()

    def hex_xor(self, a_bytes, b_bytes):
        byte_out = bytearray()
        if len(a_bytes) != len(b_bytes):
            raise ValueError("Cannot perform full XOR. byte arrays are not equal\
                              length")
        for i, byte_i in enumerate(a_bytes):
            byte_out.append(byte_i ^ b_bytes[i])
        return byte_out

    def score_decoded(self, near_plain_bytes):
        key_score = 0
        for byte_i in near_plain_bytes:
            key_score += ENGLISH_CHAR_FREQ.get(chr(byte_i).lower(), 0)
        return key_score

    def hex_xor_single_key(self, byte_array, key):
        key_arr = bytearray()
        for x in range(len(byte_array)):
            key_arr.append(key)
        return self.hex_xor(byte_array, key_arr)

    def hex_xor_repeat_key(self, byte_array, key_bytes):
        full_key = bytearray()
        key_length = len(key_bytes)
        for i in range(0, len(byte_array)):
            full_key.append(key_bytes[i % key_length])
        return self.hex_xor(byte_array, full_key)

    def break_xor_cipher(self, ciphertext):
        score_arr = []
        cipher_bytes = bytes.fromhex(ciphertext)
        for c in range(256):
            result = self.hex_xor_single_key(cipher_bytes, c)
            i_score = self.score_decoded(result)
            score_arr.append([i_score, result])
        score_arr.sort(key=lambda x: x[0], reverse=True)
        return score_arr[0]

    def encrypt_rep_xor(self, plaintext, key):
        key_bytes = bytes(key, 'utf-8')
        input_bytes = bytes(plaintext, 'utf-8')
        result = self.hex_xor_repeat_key(input_bytes, key_bytes)
        return result

    def hamming_distance(self, text_1, text_2):
        bytes_1 = list(map(bin, text_1))
        bytes_2 = list(map(bin, text_2))
        distance = 0
        if len(bytes_1) != len(bytes_2):
            raise ValueError("Cannot operate on unequal length strings")
        for b1_i, b2_i in zip(bytes_1, bytes_2):
            b_byte1 = b1_i[2:].zfill(8)
            b_byte2 = b2_i[2:].zfill(8)
            distance += sum(b1 != b2 for b1, b2 in zip(b_byte1, b_byte2))
        return distance
