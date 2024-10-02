class Solution:
    def isTriangular(self, n):
        import math as mt
        i = mt.floor(mt.sqrt(2 * n))

        if i * (i + 1) // 2 == n:
            return 1

        return 0


# {
# Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.isTriangular(N))
# } Driver Code Ends