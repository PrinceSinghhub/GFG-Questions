class Solution:
    def countBT(self, h):
        dp = [0 for i in range(h + 1)]

        dp[1] = 1
        dp[2] = 3

        for i in range(3, h + 1):
            dp[i] = ((dp[i - 1]) ** 2 + 2 * (dp[i - 1]) * (dp[i - 2])) % 1000000007

        return dp[h] % 1000000007


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        h = int(input())

        ob = Solution()
        print(ob.countBT(h))
# } Driver Code Ends