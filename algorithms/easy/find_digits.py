# https://www.hackerrank.com/challenges/find-digits/problem

# 1 

def findDigits(n: int) -> int:
    res, num = 0, n
    
    while num != 0:
        t = num % 10
        
        if t != 0 and n % t == 0:
            res += 1
        
        num //= 10
            
    return res

# 2

def findDigits(n: int) -> int:
    s = str(n)
    res = 0
    
    for l in s:
        if l != "0" and n % int(l) == 0:
            res += 1
            
    return res