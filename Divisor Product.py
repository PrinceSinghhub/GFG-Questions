class Solution:
    def divisorProduct(self, N):

        mod = 10 ** 9 + 7
        ans = 1

        for i in range(2, N + 1):
            if N % i == 0:
                ans *= i
        return ans % mod


# {
#  Driver Code Starts
# Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.divisorProduct(N))