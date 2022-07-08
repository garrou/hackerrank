# https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k: int, height: list[int]) -> int:
    maxi = max(height)
    return 0 if k > maxi else maxi - k