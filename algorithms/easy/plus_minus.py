# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr: list[int]) -> None:
    result, l = [0] * 3, len(arr)
    
    for elt in arr:
        if elt > 0:
            result[0] += 1
        elif elt < 0:
            result[1] += 1
        else:
            result[2] += 1
            
    [print(x / l) for x in result]