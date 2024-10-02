class Solution:
	def longestIncreasingPath(self, mat):

		n = len(mat)
		m = len(mat[0])
		dp = {}

		def dfs(i,j):
			if (i,j) in dp:
				return dp[(i,j)]
			for di,dj in [[-1,0],[1,0],[0,1],[0,-1]]:
				if 0<=i+di<n and 0<=j+dj<m and mat[i][j]<mat[i+di][j+dj]:
					dp[(i,j)] = max(dp.get((i,j),0),dfs(i+di,j+dj))
			dp[(i,j)] = dp.get((i,j),0)+1
			return dp[(i,j)]

		ans = 0
		for i in range(n):
			for j in range(m):
				ans = max(ans,dfs(i,j))
		return ans