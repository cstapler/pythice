def quicksort(arr):
    if len(arr) < 2:
        return arr
    left = []
    right = []
    equal = []
    pivot = arr[0]
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
        else:
            equal.append(x)
    sorted_left = quicksort(left)
    sorted_right = quicksort(right)
    resultArr = sorted_left + equal + sorted_right
    print(*resultArr)
    return resultArr


def main():
    n_input = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    quicksort(arr)


if __name__ == '__main__':
    main()
