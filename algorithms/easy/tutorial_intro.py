# https://www.hackerrank.com/challenges/tutorial-intro/problem

def introTutorial(V: int, arr: list[int]) -> int:
    start = 0 
    end = len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2    
        
        if arr[mid] < V:
            start = mid + 1
        elif arr[mid] > V:
            end = mid - 1
        else:
            return mid
    
    return -1   