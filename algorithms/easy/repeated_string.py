# https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s: str, n: int) -> int:
    l = len(s)
    # s[:n % l] -> case of odd length, need to check if first letter is 'a'
    return n // l * s.count('a') + s[:n % l].count('a') 