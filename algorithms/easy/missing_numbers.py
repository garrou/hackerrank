# https://www.hackerrank.com/challenges/missing-numbers/problem

def missingNumbers(arr: list[int], brr: list[int]) -> list[int]:
    res = {} 
    d_arr = count_occurs(arr)         
    d_brr = count_occurs(brr)

    for elt in brr: 
        if res.get(elt) == None and d_arr.get(elt) != d_brr.get(elt):
            res[elt] = True
    
    return sorted(res)

def count_occurs(arr: list[int]) -> dict[int, int]:
    d = {}
    
    for elt in arr:
        if d.get(elt) == None:
            d[elt] = 1
        else:
            d[elt] += 1
            
    return d