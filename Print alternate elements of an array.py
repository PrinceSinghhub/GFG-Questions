def printAl(arr, n):
    for i in range(0, n, 2):
        print(arr[i], end=" ")


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        printAl(arr, n)
        print()