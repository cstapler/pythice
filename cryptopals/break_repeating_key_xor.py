import codecs
import binascii
from itertools import combinations
from crypto import CryptoKit

xor_kit = CryptoKit()


def test():
    in_1 = bytes('this is a test', 'utf-8')
    in_2 = bytes('wokka wokka!!!', 'utf-8')
    distance = xor_kit.hamming_distance(in_1, in_2)
    assert(distance == 37)


def chunk_text_bytes(text_bytes, chunk_size):
    chunks = []
    for x in range(0, len(text_bytes), chunk_size):
        chunks.append(text_bytes[x:x+chunk_size])
    return chunks


def transpose_chunks(chunks):
    # print("chunk {}".format(len(chunks[0])).center(60, '-'))
    new_chunks = [[] for _ in range(len(chunks[0]))]
    for i, chunk in enumerate(chunks):
        for j, piece in enumerate(chunk):
            new_chunks[j].append(piece)
    return list(map(bytearray, new_chunks))


def main():
    results = []
    possible = []
    with open('inputs1c6.txt', 'rb') as in_file:
        text_bytes = codecs.decode(in_file.read(), 'base64')
        for key_size in range(2, 40):
            key_distances = []
            text_chunked = chunk_text_bytes(text_bytes, key_size)[:6]
            for a, b in combinations(text_chunked, 2):
                distance = xor_kit.hamming_distance(a, b)
                key_distances.append(distance / key_size)
            results.append([key_size, sum(key_distances) / len(key_distances)])
        results.sort(key=lambda x: x[1])
        for result in results[:4]:
            probable_key_size = result[0]
            text_chunks = chunk_text_bytes(text_bytes, probable_key_size)
            trans_chunks = transpose_chunks(text_chunks)

            key = bytearray()
            for i in trans_chunks:
                decoded_chunk = xor_kit.break_xor_cipher(i)
                key.append(decoded_chunk[2])
            possible.append(xor_kit.encrypt_rep_xor(text_bytes, key))
        print(max(possible, key=lambda x: xor_kit.score_decoded(x)).decode())


if __name__ == '__main__':
    test()
    main()
