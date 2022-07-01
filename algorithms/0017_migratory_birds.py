# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr: list[int]) -> int:
    d = {x: 0 for x in range(1, 6)}
    
    for elt in arr:
        d[elt] += 1

    return max(d, key=d.get)