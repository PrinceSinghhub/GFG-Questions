def Search(arr, n, k):
    if k in arr:
        return arr.index(k)

    else:
        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tcs = int(input())
    for _ in range(tcs):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())

        print(Search(arr, n, k))
