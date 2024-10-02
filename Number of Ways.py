class Solution:
    def arrangeTiles(self, N):
        dp =[0,1,1,1,2]
        if N<5:
            return dp[N]
        dp = dp +[-1]*(N-4)
        for i in range(5,N+1):
            dp[i]= dp[i-1]+dp[i-4]
        return dp[N]