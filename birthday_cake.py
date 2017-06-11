"""
Challenge:

Colleen is turning  years old! Therefore, she has  candles of various heights
on her cake, and candle  has height . Because the taller candles tower over the
shorter ones, Colleen can only blow out the tallest candles.

Given the  for each individual candle, find and print the number of candles she
 can successfully blow out.
"""
import sys


def birthdayCakeCandles(n, ar):
    max_height = 0
    tall_candle_count = 1
    for i in range(n):
        if i > max_height:
            max_height = i
            tall_candle_count = 1  # Start count over every new max is found
        else if i == max_height:
            tall_candle_count += 1


n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
