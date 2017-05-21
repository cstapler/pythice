"""
 hackerrank python ginortS challenge solution.

"""
import string


def _word_first_lower_first_odd_first(current_char):
    """Key function for sorting based on ginortS specified rules."""

    if current_char.isalpha():
        if current_char.islower():
            c_val = string.ascii_lowercase.index(current_char)
            return c_val
        c_val = string.ascii_uppercase.index(current_char)
        return c_val + 1000
    c_int = int(current_char)
    if c_int % 2 == 0:
        return c_int + 100000
    return c_int + 10000


def main():
    """Take inputted string and returns sorted string based on ginortS
    challenge rules.
    """
    input_string = input()
    output_string = sorted(input_string, key=_word_first_lower_first_odd_first)
    print(*output_string, sep='')


if __name__ == "__main__":
    main()
