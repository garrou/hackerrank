# https://www.hackerrank.com/challenges/kangaroo/problem

# kangaroo_pos = (nb_jumps * speed) + start_pos
# (nb_jumps * speed1) + start_pos1 = (nb_jumps * speed2) + start_pos2
# (start_pos1 - start_pos2) / (speed2 - speed1) = nb_jumps
def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    return "YES" if v1 > v2 and (x1 - x2) % (v2 - v1) == 0 else "NO"