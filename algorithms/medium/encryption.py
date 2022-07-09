# https://www.hackerrank.com/challenges/encryption/problem

import math

def encryption(s: str) -> str:
    s = s.replace(" ", "")
    l = len(s)
    sq = math.sqrt(l)
    rows = math.floor(sq)
    cols = math.ceil(sq)
    total = rows * cols
    
    if total < l:
        rows += l - total

    ind = 0
    grid = [[""] * cols for _ in range(rows)] 

    for i in range(rows):
        for j in range(cols):
            if ind < l:
                grid[i][j] = s[ind]
            ind += 1
        
    res = ""

    for i in range(cols):
        for j in range(rows):
            res += grid[j][i] 
        res += " "
            
    return res