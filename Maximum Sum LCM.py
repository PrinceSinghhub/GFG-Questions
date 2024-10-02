import math


class Solution:
    def lcm(self, a, b):
        return (a * b) // math.gcd(a, b)

    def maxSumLCM(self, n):
        # code here
        ans = 0
        for i in range(1, int(math.sqrt(n)) + 1):
            if self.lcm(i, n) == n:
                ans += (i + n // i)
        if int(math.sqrt(n)) ** 2 == n:
            # check if n is a perfect square
            return ans - int(math.sqrt(n))
        return ans

    # {


# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.maxSumLCM(n))
# } Driver Code Ends