"""Given a string with spaces replaces the spaces with dashes
"""


def split_and_join(line: str):
    return line.replace(" ", "-")


def main():
    input_line = input()
    print(split_and_join(input_line))


if __name__ == '__main__':
    main()
