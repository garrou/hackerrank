# https://www.hackerrank.com/challenges/picking-numbers/problem

def pickingNumbers(a: list[int]) -> int:
    l, res, = len(a), 0
    
    for i in range(l):
        # [a[i] - 1, a[i] + 1]
        cur = [a[j] for j in range(i, l) if abs(a[j] - a[i]) <= 1]      
        d = {-1: 0, 1: 0}
                
        for elt in cur:
            if elt < a[i]:
                d[-1] += 1
            elif elt > a[i]:
                d[1] += 1
            else:
                d[-1] += 1
                d[1] += 1
        
        maxi = max(d.values())
        res = maxi if maxi > res else res
    
    return res
