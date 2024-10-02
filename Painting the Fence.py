# User function Template for python3

class Solution:
    def countWays(self, n, k):
        dp = [k, k ** 2, k ** 3 - k] + [0] * (n - 3)
        mod = 10 ** 9 + 7

        for i in range(3, n):
            dp[i] = (k * dp[i - 1] - (k - 1) * dp[i - 3]) % mod

        return dp[n - 1]


# {
# Driver Code Starts

# Initial Template for Python 3


t = int(input())
for _ in range(0, t):
    x = list(map(int, input().split()))
    n = x[0]
    k = x[1]
    ob = Solution()
    ans = ob.countWays(n, k)
    print(ans)

# } Driver Code Ends