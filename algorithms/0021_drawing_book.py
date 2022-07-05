# https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n: int, p: int) -> int:
    front = p // 2
    prev_mult = p - (2 - p) % 2
    back = (n - prev_mult) // 2 
    return min(front, back)
