class Solution:
    # function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        if len(C) != len(A) + len(B):
            return False

        dp = [[None for i in range(len(B) + 1)] for i in range(len(A) + 1)]
        dp[0][0] = True

        for i in range(1, len(A) + 1):
            dp[i][0] = dp[i - 1][0] and (A[i - 1] == C[i - 1])

        for j in range(1, len(B) + 1):
            dp[0][j] = dp[0][j - 1] and (B[j - 1] == C[j - 1])

        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                x = dp[i - 1][j] and (A[i - 1] == C[i + j - 1])
                y = dp[i][j - 1] and (B[j - 1] == C[i + j - 1])

                dp[i][j] = (x or y)
        return dp[-1][-1]