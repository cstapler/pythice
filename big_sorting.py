
def main():
    """Implement Bucktsort on an array with really big numbers

       Puts numbers into buckets based on their length
    """
    number_input = int(input())
    buckets = {}
    for _ in range(number_input):
        item = input().strip()
        item_len = len(item)
        if item_len not in buckets:
            buckets[item_len] = []
        buckets[item_len].append(item)

    for bucket_key in sorted(buckets):
        for number in sorted(buckets[bucket_key]):
            print(number)


if __name__ == "__main__":
    main()
