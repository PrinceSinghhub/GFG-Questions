class Solution:
	def minPoints(self, M, N, points):
	    dp=[[0 for _ in range(N)]for _ in range(M)]
        for i in range(M-1,-1,-1):
            for j in range(N-1,-1,-1):
                if i==M-1 and j==N-1:dp[i][j]=max(1-points[i][j],1)
                elif i==M-1:dp[i][j]=max(dp[i][j+1]-points[i][j],1)
                elif j==N-1:dp[i][j]=max(dp[i+1][j]-points[i][j],1)
                else:dp[i][j]=max(min(dp[i+1][j]-points[i][j],dp[i][j+1]-points[i][j]),1)
        return dp[0][0]