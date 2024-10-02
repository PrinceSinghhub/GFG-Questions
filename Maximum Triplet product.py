# User function Template for python3

class Solution:
    def maxTripletProduct(self, arr, n):
        arr.sort()
        return max(arr[0] * arr[1] * arr[n - 1], arr[n - 1] * arr[n - 2] * arr[n - 3])
        # Complete the function


# {
# Driver Code Starts
# Initial Template for Python 3

import sys

for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    res = ob.maxTripletProduct(arr, n)
    print(res)
# } Driver Code Ends