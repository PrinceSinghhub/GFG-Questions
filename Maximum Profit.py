class Solution:
    def maxProfit(self, K, N, A):
        # code here

        dp = [0] * N

        for tns in range(K):
            pos = -A[0]
            profit = 0
            for i in range(1, N):
                pos = max(pos, dp[i] - A[i])
                profit = max(profit, pos + A[i])
                dp[i] = profit
        return dp[-1]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])

        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends