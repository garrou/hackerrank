# https://www.hackerrank.com/challenges/insertionsort2/problem

def insertionSort2(n: int, arr: list[int]):
    for i in range(1, n):
        j = i
        key = arr[i]
        while j > 0 and arr[j - 1] > key:
           arr[j] = arr[j-1]
           j -= 1
        arr[j] = key
        
        for elt in arr:
            print(elt, end=' ')
        print()