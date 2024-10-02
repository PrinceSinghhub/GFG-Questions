class Solution:
    ##Complete this function
    def ternarySearch(self, arr, N, K):
        if K in arr:
            return 1
        return -1
        # Your code here


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        NK = input().strip().split()
        N = int(NK[0])
        K = int(NK[1])
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.ternarySearch(arr, N, K))