class Solution:
    def match(self, wild, pattern):
        # code here
        s = pattern
        p = wild
        m = len(s)
        n = len(p)
        dp = [["."] * (n + 1) for i in range(m + 1)]

        for i in range(m + 1):
            for j in range(n + 1):

                if i == 0 and j == 0:
                    dp[i][j] = True

                if j == 0 and i > 0:
                    dp[i][j] = False

                if i == 0 and j > 0:
                    if p[j - 1] == "*":
                        dp[i][j] = dp[i][j - 1]

                    else:
                        dp[i][j] = False

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] = dp[i - 1][j - 1]

                elif p[j - 1] == "*":
                    dp[i][j] = (dp[i][j - 1] or dp[i - 1][j] or dp[i - 1][j - 1])

                else:
                    dp[i][j] = False

        # print(dp)
        return dp[-1][-1]

    # {


# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        wild = input()
        pattern = input()

        ob = Solution()
        if (ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends