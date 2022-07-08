# https://www.hackerrank.com/challenges/angry-professor/problem

def angryProfessor(k: int, a: list[int]) -> str:
    ok = len([x for x in a if x <= 0])
    return "NO" if ok >= k else "YES"