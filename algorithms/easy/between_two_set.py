# https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a: list[int], b: list[int]) -> int:
    res = 0
    l_a = len(a)
    l_b = len(b)
    
    for i in range(a[l_a - 1], b[0]+1):
        is_factor = True
        j = 0
        
        while j < l_a and is_factor:
            if i % a[j] != 0:
                is_factor = False
            j += 1
        
        j = 0
        while j < l_b and is_factor:
            if b[j] % i != 0:
                is_factor = False
            j += 1
            
        if is_factor:
            res += 1
            
    return res