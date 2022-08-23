# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s: str, t: str, k: int) -> str:
    ls = len(s)
    lt = len(t)
    i = 0
    
    # prefix length
    while i <= ls - 1 and i <= lt - 1 and s[i] == t[i]:
        i += 1
        
    if k >= ls + lt:
        return "Yes"
    # check and simulate append delete 
    elif k >= ls + lt - 2 * i and (k - ls - lt + 2 * i) % 2 == 0:
        return "Yes"
    else:
        return "No"