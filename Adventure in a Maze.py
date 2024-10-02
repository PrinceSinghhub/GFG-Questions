class Solution:
    def FindWays(self, matrix):
         # Code here
         dp = [[[0,0] for _ in range(len(matrix))] for _ in range(len(matrix))]
         dp[0][0]=[1,0]
         for i in range(len(matrix)):
             for j in range(len(matrix)):
                 if i>0 and matrix[i-1][j] in (2,3):
                     dp[i][j][0]+=dp[i-1][j][0]
                     dp[i][j][1]=max(dp[i][j][1],dp[i-1][j][1])
                 if j>0 and matrix[i][j-1] in (1,3):
                     dp[i][j][0]+=dp[i][j-1][0]
                     dp[i][j][1]=max(dp[i][j][1],dp[i][j-1][1])
                 if dp[i][j][0]>0:
                     dp[i][j][0]%=1000000007
                     dp[i][j][1]+=matrix[i][j]
         return dp[-1][-1]

#{
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			cur = list(map(int, input().split()))
			matrix.append(cur)
		obj = Solution()
		ans = obj.FindWays(matrix)
		for _ in ans:
			print(_, end = " ")
		print()