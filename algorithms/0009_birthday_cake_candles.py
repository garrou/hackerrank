# https://www.hackerrank.com/challenges/birthday-cake-candles/problem

def birthdayCakeCandles(candles: list[int]) -> int:
    maxi = max(candles)
    return candles.count(maxi)