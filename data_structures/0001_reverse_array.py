# https://www.hackerrank.com/challenges/arrays-ds/problem

def reverseArray(a: list[int]) -> list[int]:
    l = len(a)
    for i in range(l // 2):
        temp = a[i]
        a[i] = a[l-i-1] 
        a[l-i-1] = temp
        
    return a