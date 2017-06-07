import re


def main():
    n_count = int(input())  # Number of inputs
    for i in range(0, n_count):
        number_input = input()
        print(bool(re.match(r'^[\+-]?\d*\.\d+$', number_input)))

if __name__ == '__main__':
    main()
