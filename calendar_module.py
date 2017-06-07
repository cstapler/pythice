import calendar


def main():
    date_input = input()  # expect input to be string formatted MM DD YYYY
    date_array = date_input.split()
    day_of_week = calendar.weekday(int(date_array[2]), int(date_array[0]),
                                   int(date_array[1]))
    print(calendar.day_name[day_of_week].upper())


if __name__ == '__main__':
    main()
