# User function Template for python3
class Solution:

    def SpaceOptimizationApproch(self, str1, index1, str2, index2, prev, curr):

        '''we will all ready 0th row and 0th collom inelisized with 0 like in tablulation
        So here no need to re-write again we just start iteration with 1'''

        for indx1 in range(1, index1 + 1):
            for indx2 in range(1, index2 + 1):

                if str1[indx1 - 1] == str2[indx2 - 1]:
                    curr[indx2] = 1 + prev[indx2 - 1]

                else:
                    pick = prev[indx2]
                    notPick = curr[indx2 - 1]
                    curr[indx2] = max(pick, notPick)

            prev[:] = curr

        return prev[index2]

    def longestCommonSubsequence(self, str1, str2):

        n = len(str1)
        m = len(str2)
        prev = [0] * (m + 1)
        curr = [0] * (m + 1)
        return self.SpaceOptimizationApproch(str1, n, str2, m, prev, curr)

    def minOperations(self, s1, s2):
        LCS = self.longestCommonSubsequence(s1, s2)
        n = len(s1)
        m = len(s2)

        numberOfDeletion = n - LCS
        numberOfInsertion = m - LCS
        totalNumberOfOperation = (n + m) - 2 * LCS
        return totalNumberOfOperation