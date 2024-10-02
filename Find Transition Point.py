def transitionPoint(arr, n):
    start = 0
    end = n-1
    answer = -1
    while start <= end :
        if arr[start]==1:
            return start
        start += 1

    return answer

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(transitionPoint(arr, n))