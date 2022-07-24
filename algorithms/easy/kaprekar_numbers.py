# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

def kaprekarNumbers(p: int, q: int) -> None:
    res = []

    if p < 10:
        if p <= 1:
            res.append(1)
        res.append(9)
        p = 45
    
    for i in range(p, q+1):
        s = str(i**2)
        l = len(s)
        
        if int(s[:l//2]) + int(s[l//2:]) == i:
            res.append(i)
            
    if len(res) == 0:
        print('INVALID RANGE')
    else:
        for elt in res:
            print(elt, end=' ')