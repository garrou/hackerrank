# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

def divisibleSumPairs(n: int, k: int, ar: list[int]) -> int:
    res = 0
    
    for i in range(len(ar)):
        for j in range(1, len(ar)):
            if i < j and (ar[i] + ar[j]) % k == 0:
                res += 1
    return res