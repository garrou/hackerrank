# https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill: list[int], k: int, b: int):
    ana = (sum(bill) - bill[k]) // 2
    print("Bon Appetit") if ana == b else print(f"{b - ana}")