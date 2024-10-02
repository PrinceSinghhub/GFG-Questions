import numpy as np
def findMaxProduct(arr, n, m):
    prod=0
    for i in range(n):
        b=np.array(arr[i:i+m])
        b=np.prod(b)
        if b>prod:
            prod=b
    return prod

#{
#  Driver Code Starts
# Your code goes here
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,m = map(int, input().strip().split(' '))
        arr = list(map(int, input().strip().split()))
        print (findMaxProduct(arr, n, m))