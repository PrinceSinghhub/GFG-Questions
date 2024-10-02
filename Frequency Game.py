# User function Template for python3


def LargButMinFreq(arr, n):
    map = {}

    for i in arr:
        if i not in map:
            map[i] = 1
        else:
            map[i] += 1

    Max = -10 ** 9
    count = 10 ** 9

    for val, ind in map.items():
        if val > Max and ind < count:
            count = ind
            Max = val
        elif val < Max and ind < count:
            count = ind
            Max = val
        elif val > Max and ind == count:
            count = ind
            Max = val

    return Max


# {
# Driver Code Starts
# Initial Template for Python 3

t = int(input())
# Iterating over test cases
for _ in range(t):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(LargButMinFreq(arr, n))
# } Driver Code Ends