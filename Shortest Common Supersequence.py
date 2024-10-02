# User function Template for python3

class Solution:

    def printSCSusingArray(self, str1, index1, str2, index2, dp, array, ansLen):

        arrIndx = ansLen - 1

        # todo backtracking in the dp table
        ind1 = index1
        ind2 = index2

        while ind1 > 0 and ind2 > 0:

            if str1[ind1 - 1] == str2[ind2 - 1]:
                array[arrIndx] = str1[ind1 - 1]
                ind1 -= 1
                ind2 -= 1
                arrIndx -= 1

            elif dp[ind1 - 1][ind2] > dp[ind1][ind2 - 1]:
                array[arrIndx] = str1[ind1 - 1]
                arrIndx -= 1
                ind1 -= 1

            else:
                array[arrIndx] = str2[ind2 - 1]
                arrIndx -= 1
                ind2 -= 1

        # its may be the ind1 or indx2 is remaing the Char for the finding the possible SCS then

        while ind1 > 0:
            array[arrIndx] = str1[ind1 - 1]
            arrIndx -= 1
            ind1 -= 1

        while ind2 > 0:
            array[arrIndx] = str2[ind2 - 1]
            arrIndx -= 1
            ind2 -= 1

        # reform array into the string
        SCS = "".join(array)
        return SCS

    def printSCSusingString(self, str1, index1, str2, index2, dp):

        SCS = ""

        # todo backtracking in the dp table
        ind1 = index1
        ind2 = index2

        while ind1 > 0 and ind2 > 0:

            if str1[ind1 - 1] == str2[ind2 - 1]:
                SCS += str1[ind1 - 1]
                ind1 -= 1
                ind2 -= 1

            elif dp[ind1 - 1][ind2] > dp[ind1][ind2 - 1]:
                SCS += str1[ind1 - 1]
                ind1 -= 1

            else:
                SCS += str2[ind2 - 1]
                ind2 -= 1

        # its may be the ind1 or indx2 is remaing the Char for the finding the possible SCS then

        while ind1 > 0:
            SCS += str1[ind1 - 1]
            ind1 -= 1

        while ind2 > 0:
            SCS += str2[ind2 - 1]
            ind2 -= 1

        return SCS

    def TabulationApproch(self, str1, index1, str2, index2, dp):

        for i in range(index1 + 1):
            dp[i][0] = 0

        for j in range(index2 + 1):
            dp[0][j] = 0

        for indx1 in range(1, index1 + 1):
            for indx2 in range(1, index2 + 1):

                if str1[indx1 - 1] == str2[indx2 - 1]:
                    dp[indx1][indx2] = 1 + dp[indx1 - 1][indx2 - 1]

                else:
                    pick = dp[indx1 - 1][indx2]
                    notPick = dp[indx1][indx2 - 1]
                    dp[indx1][indx2] = max(pick, notPick)

        # todo print the our tabulation table how look like that
        # for tab in dp:
        #     print(tab)

        # todo Base Case if the Not any LCS Possible then Simply Return ""
        ansLen = dp[index1][index2]
        if ansLen == 0:
            return index1 + index2

        # todo but this gives the reversed answer we want to re-reverse for the correct ans
        # SCS = self.printSCSusingString(str1, index1, str2, index2, dp)
        # print("Stering: ", SCS)
        # SCS = SCS[::-1]
        # return SCS
        # todo Recureter not happy to use this in-build function then we Go with the Array Approch
        LCS = dp[index1][index2]

        # our array len is the (index1+index2) - LCS according to the Recursion Approch
        arrLen = (index1 + index2) - LCS
        array = [0] * arrLen
        # print(array)
        SCS = self.printSCSusingArray(str1, index1, str2, index2, dp, array, arrLen)
        # print("Array: ", SCS)

        return len(SCS)

    def ShortestCommonSupersequence(self, str1, str2):

        n = len(str1)
        m = len(str2)
        dp = []
        for _ in range(n + 1):
            arr = [-1] * (m + 1)
            dp.append(arr)

        return self.TabulationApproch(str1, n, str2, m, dp)

    # Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):

        return self.ShortestCommonSupersequence(X, Y)


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        X, Y = input().split()

        print(Solution().shortestCommonSupersequence(X, Y, len(X), len(Y)))

# } Driver Code Ends