class Solution:
    def findHeight(self, N, arr):
        # code here

        x = arr[N - 1]
        h = 1

        while arr[x] != -1:
            x = arr[x]
            h += 1
        return h + 1


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])