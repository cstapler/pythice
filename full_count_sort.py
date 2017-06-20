#!/usr/bin/env python3

def count_sort(input_arr):
    count_arr = [0 for j in range(100)]
    arr_length = len(input_arr)
    for arr_index, obj_tup in enumerate(input_arr):
        if arr_index < arr_length / 2:
            input_arr[arr_index] = tuple([obj_tup[0], '-'])
        count_arr[int(obj_tup[0])] += 1

    last_count_sum = 0
    for index, count in enumerate(count_arr):
        if index != 0:
            last_count_sum = count_arr[index - 1]
        count_arr[index] += last_count_sum

    output_arr = [0 for k in input_arr]
    for num, value in reversed(input_arr):
        output_arr[count_arr[int(num)]-1] = value
        count_arr[int(num)] -= 1
    return output_arr

def main():
    num_lines = int(input())
    input_list = [tuple(input().strip().split()) for i in range(num_lines)]
    new_arr = count_sort(input_list)
    print(*new_arr)


if __name__ == "__main__":
    main()
