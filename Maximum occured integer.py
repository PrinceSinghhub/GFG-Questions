class Solution:
    # Complete this function
    # Function to find the maximum occurred integer in all ranges.
    def maxOccured(self, L, R, N, maxx):
        m = max(R) + 1
        arr = [0 for i in range(m + 1)]

        for i in L:
            arr[i] += 1
        for j in R:
            arr[j + 1] -= 1

        # msum = arr[0]
        for i in range(1, m, 1):
            arr[i] = arr[i] + arr[i - 1]

        v = arr.index(max(arr))
        return v


# {
# Driver Code Starts
# Initial Template for Python 3


import math

A = [0] * 1000000


def main():
    T = int(input())

    while (T > 0):
        global A
        A = [0] * 1000000

        N = int(input())

        L = [int(x) for x in input().strip().split()]
        R = [int(x) for x in input().strip().split()]

        maxx = max(R)
        ob = Solution()
        print(ob.maxOccured(L, R, N, maxx))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends