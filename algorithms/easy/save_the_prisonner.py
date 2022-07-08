# https://www.hackerrank.com/challenges/save-the-prisoner/problem

def saveThePrisoner(n: int, m: int, s: int) -> int:
    if n == 1:
        return 1
    elif m == 1:
        return s
    
    res = (s + (m % n) - 1) % n
    return res if res > 0 else n