# # https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s: str) -> int:
    # 90 == 'Z'
    return len([x for x in s if ord(x) <= 90]) + 1
