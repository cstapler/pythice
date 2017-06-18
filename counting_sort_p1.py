#!/usr/bin/env python3


def main():
    _ = input()
    input_list = [int(i) for i in input().strip().split()]
    count_arr = [0 for j in range(100)]
    for num in input_list:
        count_arr[num] += 1
    print(*count_arr, sep=" ")

if __name__ == "__main__":
    main()
