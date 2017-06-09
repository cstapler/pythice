"""The Power Sum Challenge
Find the number of ways that a given integer, X, can be expressed as the sum
of the Nth power of unique, natural numbers.
"""


def main():
    total = int(input())
    n_input = int(input())
    n_start = 1
    print(find_sum_expression(total, n_input, n_start))


def find_sum_expression(total, n, n_start):
    sub_sum = total - pow(n_start, n)
    if sub_sum == 0:
        return 1
    elif sub_sum < 0:
        return 0
    else:
        return (find_sum_expression(sub_sum, n, n_start + 1) +
                find_sum_expression(total, n, n_start + 1))


if __name__ == '__main__':
    main()
