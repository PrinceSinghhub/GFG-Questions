#User function Template for python3
class Solution:
    def numberOfPaths(self, m, n):
        dp = [[1] * n for x in range(m)]
        for i in range(1,m):

            for j in range(1,n):

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]%(10**9+7)



#{
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m,n = input().split()
		m=int(m)
		n=int(n)
		ob = Solution();
		print(ob.numberOfPaths(m,n))

# } Driver Code Ends