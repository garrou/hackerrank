# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c: list[int]) -> int:
    res, i = 0, 0
    l = len(c)
    
    while i < l - 2:
        i = i + 1 if c[i+2] else i + 2
        res += 1

    return res + 1 if i < l - 1 else res