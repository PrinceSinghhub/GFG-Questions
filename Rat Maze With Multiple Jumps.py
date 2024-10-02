class Solution:
	def ShortestDistance(self, matrix):
		n = len(matrix)
		MAX = 10**9+7
		ans = [[0]*n for i in range(n)]
		def go(i,j):
			if i==n-1 and j==n-1:

				ans[i][j]=1
				return True
			if i>=n or j>=n or matrix[i][j]==0:
				return False
			jump = matrix[i][j]
			for t in range(1,jump+1):
				if go(i,j+t):
					ans[i][j]=1
					return True
				if go(i+t,j):
					ans[i][j]=1
					return True
			return False
		if go(0,0):
			return ans
		return [[-1]]

ans = Solution()
arr = [[2,1,0,0],[3,0,0,1],[0,1,0,1],
[0,0,0,1]]
print(ans.ShortestDistance(arr))