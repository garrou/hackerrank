# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades: list[int]) -> list[int]:
    res = []
    
    for g in grades:
        next_mult = g + (5 - g) % 5
        if g >= 38 and next_mult - g < 3:
            g = next_mult
        res.append(g)
    return res