# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

def squares(a:int , b: int) -> int:
    res = 0
    inf = int(math.sqrt(a))
    sup = int(math.sqrt(b))
    
    for i in range(inf, sup+1):
        k = i * i
        if k >= a and k <= b:
            res += 1
        
    return res