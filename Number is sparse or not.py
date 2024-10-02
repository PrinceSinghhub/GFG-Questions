class Solution:

    # Function to check if the number is sparse or not.
    def isSparse(self, n):

        Bin = bin(n)[2::]

        Bin = str(int(Bin))

        for i in range(len(Bin) - 1):

            if Bin[i] == '1' and Bin[i + 1] == '1':
                return 0

        return 1

ans = Solution()
print(ans.isSparse(3))