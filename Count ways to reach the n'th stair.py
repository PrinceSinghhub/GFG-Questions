#User function Template for python3

class Solution:
    def countWays(self,n):
        mod = 1000000007
        dp = [-1]*(n+5)
        def solve(n,dp):
            if n<=2:
                dp[n] = n
                return dp[n]
            if dp[n] != -1:
                return dp[n]
            dp[n] = (solve(n-1,dp)%mod + solve(n-2,dp)%mod) % mod
            return dp[n]
        return solve(n,dp)