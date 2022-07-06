# https://www.hackerrank.com/challenges/strange-advertising/problem

def viralAdvertising(n: int) -> int:
    liked, cumulative = 2, 2
    
    for i in range(0, n-1):
        shared = liked * 3
        liked = shared // 2
        cumulative += shared // 2
        
    return cumulative