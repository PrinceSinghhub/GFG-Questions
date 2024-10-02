# User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self, S):
        # code here
        n = len(S)
        c = 0
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        s1 = S
        s2 = S[::-1]
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return n - dp[n][n]


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends