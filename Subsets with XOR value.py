import math
class Solution:
    def subsetXOR(self, arr, N, k):
        # code here
        dp = [[0 for i in range(128)] for j in range(N+1)]
        print(dp)
        dp[0][0] = 1
        for i in range(1,N+1):
            for j in range(128):
                dp[i][j] = dp[i-1][j] + dp[i-1][j^arr[i-1]]
        return dp[N][k]


ans = Solution()
arr = [6,9,4,2]
print(ans.subsetXOR(arr,4,6))
