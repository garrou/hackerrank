# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(ar: list[int]) -> int:
    return sum(ar)

def simpleArraySum(ar: list[int]) -> int:
    res = 0
    for elt in ar:
        res += elt
    return res