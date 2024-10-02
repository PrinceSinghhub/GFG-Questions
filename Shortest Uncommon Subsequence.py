class Solution:
    def __init__(self):
        self.indices = {}

    def shortestUnSub(self, S, T):
        m = len(S)
        n = len(T)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = 501

        for i in range(1, m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                k = j - 1
                ch = S[i - 1]
                if (ch == T[k]):
                    self.indices[ch] = k
                elif (ch in self.indices):
                    k = self.indices[ch]
                else:
                    while (k >= 0):
                        if (T[k] == S[i - 1]):
                            break
                        k -= 1
                    self.indices[ch] = k
                if (k == -1):
                    dp[i][j] = 1

                else:
                    dp[i][j] = min(dp[i - 1][j], 1 + dp[i - 1][k])
                ans = dp[i][j]
                if ans >= 501:
                    ans = -1
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S, T = map(str, input().split())

        ob = Solution()
        print(ob.shortestUnSub(S, T))
# } Driver Code Ends