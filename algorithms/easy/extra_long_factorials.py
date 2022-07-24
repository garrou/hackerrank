# https://www.hackerrank.com/challenges/extra-long-factorials/problem

def extraLongFactorials(n: int) -> None:
    res = n
    
    while n > 1:
        n -= 1
        res *= n
        
    print(res)