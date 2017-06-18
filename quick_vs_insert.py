#!/usr/bin/env python3

swap_num = 0

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


def partition(arr, lower, higher):
    global swap_num
    pivot = arr[higher]
    i = lower - 1
    for j in range(lower, higher):
        if arr[j] <= pivot:
            swap_num += 1
            i += 1
            if i != j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    swap_num += 1
    temp = arr[i + 1]
    arr[i + 1] = arr[higher]
    arr[higher] = temp
    return i + 1


def quicksort(arr, lower, higher):
    global swap_num
    if lower < higher:
        last_piv = partition(arr, lower, higher)
        quicksort(arr, lower, last_piv - 1)
        quicksort(arr, last_piv + 1, higher)
        return swap_num
    return 0


_ = int(input().strip())
arr_insert = [int(num) for num in input().strip().split()]
arr_quick = arr_insert.copy()
shifted_sum = insertion_sort(arr_insert)
swap_sum = quicksort(arr_quick, 0, len(arr_quick) - 1,)
print("shifted " + str(shifted_sum))
print("swapped " + str(swap_num))
print(shifted_sum - swap_num)
