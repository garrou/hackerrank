# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

def kaprekarNumbers(p: int, q: int) -> None:
    res = []
    
    for i in range(p, q+1):
        s = str(i**2)
        l = len(s)
        left = s[:l//2]
        right = s[l//2:]
        
        if left == '':
            left = 0
        if right == '':
            right = 0
        
        if int(left) + int(right) == i:
            res.append(i)
            
    if len(res) == 0:
        print('INVALID RANGE')
    else:
        for elt in res:
            print(elt, end=' ')