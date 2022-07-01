# https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s: list[int], d: int, m: int) -> int:

    l = len(s)

    if l == 1:
        return l if s[0] == d and m == l else 0

    res = 0
    
    for i in range(l):
        current = sum(s[i:i+m])
        if current == d:
            res += 1
    
    return res