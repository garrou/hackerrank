# https://www.hackerrank.com/challenges/strange-code/problem

def strangeCounter(t: int) -> int:
    res = 0
    count = 0
    
    while res < t:
        res += 3 * (2 ** count)
        count += 1
        
    return res - t + 1