from crypto import CryptoKit


def main():
    xor_breaker = CryptoKit()
    all_scores = []
    with open('inputs1c4.txt', 'r') as in_file:
        for line in in_file.readlines():
            all_scores.append(xor_breaker.break_xor_cipher(line.strip()))
    all_scores.sort(key=lambda x: x[0], reverse=True)
    print(all_scores[0][1].decode())


if __name__ == '__main__':
    main()
