# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x: int, y: int, z: int) -> str:
    delta_a = abs(x - z)
    delta_b = abs(y - z)
    
    if delta_a == delta_b:
        return "Mouse C"
    else:
        return "Cat A" if delta_a < delta_b else "Cat B"
