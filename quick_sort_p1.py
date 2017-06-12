def main():
    n_input = int(input().strip())
    arr = [int(i) for i in input().strip().split()]
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

    print(*left, sep=' ', end=' ')
    print(*equal, sep=' ', end=' ')
    print(*right, sep=' ', end=' ')


if __name__ == '__main__':
    main()
