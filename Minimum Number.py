# User function Template for python3
import math


class Solution:
    def minimumNumber(self, n, arr):
        g = arr[0]
        for i in range(1, n):
            g = math.gcd(g, arr[i])
        return g


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        obj = Solution()
        print(obj.minimumNumber(n, arr))
# } Driver Code Ends