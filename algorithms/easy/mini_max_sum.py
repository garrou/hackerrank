# https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr: list[int]) -> None:
    arr.sort()
    mini = sum([arr[i] for i in range(len(arr) - 1)])
    maxi = sum([arr[i] for i in range(1, len(arr))])

    print(mini, maxi)