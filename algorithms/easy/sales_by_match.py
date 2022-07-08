# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n: int, ar: list[int]) -> int:
    d = {}
    
    for s in ar:
        d[s] = d.get(s, 0) + 1
        
    return sum(x // 2 for x in d.values())