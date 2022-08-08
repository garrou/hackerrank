# https://www.hackerrank.com/challenges/most-commons/problem

LIMIT = 3

def most_commons(s: str) -> None:
    d = {}
    
    for letter in s:
        d[letter] = d.get(letter, 0) + 1

    # sort by key and then by val
    d = {val[0] : val[1] for val in sorted(d.items(), key=lambda x: (-x[1], x[0]))[:LIMIT]}

    for k, v in d.items():
        print(f'{k} {v}')

if __name__ == '__main__':
    s = input()
    most_commons(s)