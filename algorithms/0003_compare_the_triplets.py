# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a: list[int], b: list[int]) -> list[int]:
    res = [0] * 2
    
    for i in range(len(a)):
        if a[i] > b[i]:
            res[0] += 1
        elif a[i] < b[i]:
            res[1] += 1
    return res