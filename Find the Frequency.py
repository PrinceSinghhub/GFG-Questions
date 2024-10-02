def findFrequency(arr, n, x):
    return arr.count(x)


# {
#  Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    print(findFrequency(arr, n, x))