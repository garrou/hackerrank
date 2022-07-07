# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a: list[int], k: int, queries: list[int]) -> list[int]:
    l = len(a)
    res = [0] * l
        
    for i, elt in enumerate(a):
        res[(i + k) % l] = elt

    return [res[i] for i in queries]

"""
rotate array

tmp1 = a[0]
tmp2 = a[1]

for _ in range(k):
        for i in range(1, l):
            right = (i+1) % l
            a[i] = tmp1
            tmp1 = tmp2
            tmp2 = a[right]
            a[right] = tmp1
"""