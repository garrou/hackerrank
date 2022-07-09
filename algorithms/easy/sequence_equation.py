# https://www.hackerrank.com/challenges/permutation-equation/problem

def permutationEquation(p: list[int]) -> list[int]:
    res = []
    
    for i in range(1, len(p)+1):
        res.append(p.index(p.index(i) + 1) + 1)
        
    return res