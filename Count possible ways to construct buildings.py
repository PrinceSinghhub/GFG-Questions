class Solution:
	def TotalWays(self, N):
		m = (10**9)+7
		dp =[0,2,3]+[0]*(N-2)
		for i in range(3,N+1):
			dp[i] = (dp[i-1]+dp[i-2])%m
		return (dp[N]*dp[N])%m