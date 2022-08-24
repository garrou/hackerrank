# https://www.hackerrank.com/challenges/service-lane/problem

def serviceLane(n, cases):
    res = []
    
    for c in cases:
        x, y = c
        res.append(min(width[x:y+1]))
    
    return res