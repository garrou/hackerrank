# https://www.hackerrank.com/challenges/minimum-distances/problem

def minimumDistances(a: list[int]) -> int:
    l = len(a)
    res = l
    
    for i in range(l):
        j = i + 1
        while j < l and a[j] != a[i]:
            j += 1
            
        if j != l and j - i < res:
            res = j - i
            
    return -1 if res == l else res