# https://www.hackerrank.com/challenges/time-conversion/problem

def timeConversion(s: str) -> str:
    hours, mins, s = s.split(":")
    secs, meri = s[:2], s[2:]
    h = int(hours)

    if meri == "AM":
        h %= 12
        hours = f"0{h}" if h < 10 else h
    elif h < 12:
        hours = h + 12
            
    return f"{hours}:{mins}:{secs}"