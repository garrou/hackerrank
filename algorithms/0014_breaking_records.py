# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores: list[int]) -> list[int]:
    res = [0] * 2
    mini, maxi = scores[0], scores[0]
    
    for i in range(len(scores)):
        if scores[i] > maxi:
            maxi = scores[i]
            res[0] += 1
        elif scores[i] < mini:
            mini = scores[i]
            res[1] += 1
    
    return res