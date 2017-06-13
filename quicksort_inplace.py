def partition(arr, lower, higher):
    pivot = arr[higher]
    i = lower - 1
    for j in range(lower, higher):
        if arr[j] <= pivot:
            i += 1
            if i != j:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[higher]
    arr[higher] = temp
    return i + 1


def quicksort(arr, lower, higher):
    if lower < higher:
        last_piv = partition(arr, lower, higher)
        print(*arr)
        quicksort(arr, lower, last_piv - 1)
        quicksort(arr, mid + 1, last_piv)


def main():
    n_input = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
    quicksort(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    main()
