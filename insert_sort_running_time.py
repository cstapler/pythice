#!/usr/bin/env python3

def insertion_sort(arr):
    shift_num = 0
    for i in range(1, len(arr)):
        j = i - 1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
            shift_num += 1
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return shift_num


_ = int(input().strip())
arr_to_sort = [int(num) for num in input().strip().split()]
shifted_sum = insertion_sort(arr_to_sort)
print(shifted_sum)
