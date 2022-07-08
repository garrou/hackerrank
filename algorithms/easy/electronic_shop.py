# https://www.hackerrank.com/challenges/electronics-shop/problem

def getMoneySpent(keyboards: list[int], drives: list[int], b: int) -> int:
    res = -1
    for keyboard in keyboards:
        for drive in drives:
            actual = keyboard + drive
            if actual <= b and actual > res:
                res = actual
    return res