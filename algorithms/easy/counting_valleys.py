# https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(steps: int, path: list[str]) -> int:
    res, level = 0, 0
    
    for elt in path:
        if elt == "D":
            level -= 1
        else:
            level += 1
        
        if level == 0 and elt == "U":
            res += 1
    
    return res