# https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s: int, t: int, a: int, b: int, apples: list[int], oranges: list[int]):
    apples = [ap for ap in apples if ap + a >= s and ap + a <= t]
    oranges = [o for o in oranges if o + b >= s and o + b <= t]
    print(len(apples))
    print(len(oranges))