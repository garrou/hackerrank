# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumpingOnClouds(c: list[int], k: int) -> int:
    l = len(c) 
    i = (0 + k) % l
    energy = 100
    
    while i != 0:
        if c[i] == 1:
            energy -= 2
            
        energy -= 1
        i = (i + k) % l
    
    return energy - 3 if c[0] == 1 else energy - 1