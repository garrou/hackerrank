# https://www.hackerrank.com/challenges/encryption/problem

import math

def encryption(s: str) -> str:
    s = s.replace(" ", "")
    l = len(s)
    sq = math.sqrt(l)
    rows = math.floor(sq)
    cols = math.ceil(sq)
    grid = []
    ind = 0
    total = rows * cols
    
    if total < l:
        rows += l - total

    for i in range(rows):
        grid.append([])

        for j in range(cols):
            grid[i].append(s[ind] if ind < l else "")
            ind += 1
        
    res = ""

    for i in range(cols):
        for j in range(rows):
            res += grid[j][i] 
        res += " "
            
    return res