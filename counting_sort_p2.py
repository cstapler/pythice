#!/usr/bin/env python3

def count_input(input_arr):
    count_arr = [0 for j in range(100)]
    for num in input_arr:
        count_arr[num] += 1
    return count_arr
  

def main():
    _ = input()
    input_list = [int(i) for i in input().strip().split()]
    for i, count in enumerate(count_input(input_list)):
        for j in range(count):
            print(str(i) + " ", sep="", end="")

if __name__ == "__main__":
    main()
