#User function Template for python3
class Solution:
    def __init__(self):
        self.dp = [[-1] * 1001 for _ in range(1001)]

    def solve(self, i, j, a, b, n, m):
        if i == n or j == m:
            return 0
        if self.dp[i][j] != -1:
            return self.dp[i][j]

        diff = i - j
        res = 0

        if diff < n - m:
            res = max(a[i] * b[j] + self.solve(i + 1, j + 1, a, b, n, m),
                      self.solve(i + 1, j, a, b, n, m))
        else:
            res = a[i] * b[j] + self.solve(i + 1, j + 1, a, b, n, m)

        self.dp[i][j] = res
        return res

    def maxDotProduct(self, n, m, a, b):
        return self.solve(0, 0, a, b, n, m)


#{
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n,m = int(n),int(m)
		a = [int(x) for x in input().split()]
		b = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.maxDotProduct(n,m,a,b)
		print(ans)
# } Driver Code Ends