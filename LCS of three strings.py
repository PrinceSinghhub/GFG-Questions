# User function Template for python3

# extension of the LCS

class Solution:

    def TabulationApproch(self, str1, index1, str2, index2, str3, index3, dp):

        for indx1 in range(1, index1 + 1):
            for indx2 in range(1, index2 + 1):
                for indx3 in range(1, index3 + 1):

                    if str1[indx1 - 1] == str2[indx2 - 1] and str1[indx1 - 1] == str3[indx3 - 1]:
                        dp[indx1][indx2][indx3] = (1 + dp[indx1 - 1][indx2 - 1][indx3 - 1])

                    else:
                        pick = dp[indx1 - 1][indx2][indx3]
                        notPick = dp[indx1][indx2 - 1][indx3]
                        third = dp[indx1][indx2][indx3 - 1]
                        dp[indx1][indx2][indx3] = max(pick, notPick, third)

        return dp[index1][index2][index3]

    def LCSof3(self, A, B, C, n1, n2, n3):
        dp = [[[0 for k in range(n3 + 1)] for j in range(n2 + 1)] for i in range(n1 + 1)]
        return self.TabulationApproch(A, n1, B, n2, C, n3, dp)
