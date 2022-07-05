# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem7

def beautifulDays(i: int, j: int, k: int) -> int:
    res = 0
    for n in range(i, j+1):
        if abs(n - int(str(n)[::-1])) % k == 0:
            res += 1
            
    return res