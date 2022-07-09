# https://www.hackerrank.com/challenges/utopian-tree/problem

def utopianTree(n):
    res = 1
    for i in range(n):
        res = res * 2 if i % 2 == 0 else res + 1
        
    return res