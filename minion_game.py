"""Minon game challenge
"""


def count_with_vowel(word: str):
    count = 0
    vowels = "AEIOU"
    for i, letter in enumerate(word):
        if letter in vowels:
            count += len(word) - i + 1
    return count


def count_with_consonat(word: str):
    count = 0

    return count


def minion_game(word: str):
    vowels = "AEIOU"
    stuart_score = 0
    kevin_score = 0
    for i, letter in enumerate(word):
        if letter in vowels:
            kevin_score += len(word) - i
        else:
            stuart_score += len(word) - i

    if kevin_score > stuart_score:
        print("Kevin " + str(kevin_score))
    elif kevin_score < stuart_score:
        print("Stuart " + str(stuart_score))
    else:
        print("Draw")


def main():
    input_word = 'BANANANAAAS'
    minion_game(input_word)
    print("should be draw")


if __name__ == '__main__':
    main()
