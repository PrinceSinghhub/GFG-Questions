# User function Template for python3


class Solution:
    def smallestSumSubarray(self, arr, N):
        s, mx = 0, float('inf')
        for i in arr:
            s += i
            mx = min(s, mx)
            if s > 0:
                s = 0
        return mx


# {
# Driver Code Starts
# Initial Template for Python 3


import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):
        N = int(input())

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.smallestSumSubarray(A, N))

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends