# https://www.hackerrank.com/challenges/diagonal-difference/problem

def diagonalDifference(arr: list[list[int]]) -> int:
    left, right, i, j = 0, 0, 0, len(arr) - 1
    
    for row in arr:
        left += row[i]
        i += 1
        right += row[j]
        j -= 1
        
    return abs(left - right)