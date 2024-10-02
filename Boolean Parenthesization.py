# User function Template for python3

class Solution:
    @staticmethod
    def countWays(n, s):
        mod = 1003
        symbols = list(s)
        dp = [[[0, 0] for _ in range(n)] for _ in range(n)]

        for i in range(0, n, 2):
            if symbols[i] == 'T':
                dp[i][i][1] = 1
            else:
                dp[i][i][0] = 1

        for length in range(2, n, 2):
            for i in range(n - length):
                j = i + length
                for k in range(i + 1, j, 2):
                    operator = symbols[k]
                    if operator == '&':
                        dp[i][j][1] = (dp[i][j][1] + (dp[i][k - 1][1] * dp[k + 1][j][1]) % mod) % mod
                        dp[i][j][0] = (dp[i][j][0] + ((dp[i][k - 1][0] * dp[k + 1][j][0]) % mod
                                                      + (dp[i][k - 1][0] * dp[k + 1][j][1]) % mod
                                                      + (dp[i][k - 1][1] * dp[k + 1][j][0]) % mod) % mod) % mod
                    elif operator == '|':
                        dp[i][j][0] = (dp[i][j][0] + (dp[i][k - 1][0] * dp[k + 1][j][0]) % mod) % mod
                        dp[i][j][1] = (dp[i][j][1] + ((dp[i][k - 1][1] * dp[k + 1][j][1]) % mod
                                                      + (dp[i][k - 1][0] * dp[k + 1][j][1]) % mod
                                                      + (dp[i][k - 1][1] * dp[k + 1][j][0]) % mod) % mod) % mod
                    elif operator == '^':
                        dp[i][j][1] = (dp[i][j][1] + ((dp[i][k - 1][1] * dp[k + 1][j][0]) % mod
                                                      + (dp[i][k - 1][0] * dp[k + 1][j][1]) % mod) % mod) % mod
                        dp[i][j][0] = (dp[i][j][0] + ((dp[i][k - 1][1] * dp[k + 1][j][1]) % mod
                                                      + (dp[i][k - 1][0] * dp[k + 1][j][0]) % mod) % mod) % mod

        return dp[0][n - 1][1]


# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.countWays(N, S))
# } Driver Code Ends