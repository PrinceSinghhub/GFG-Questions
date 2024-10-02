class Solution:
    def removeSpecialCharacter(self, S):

        ans = ""
        for i in S:
            if i.isalpha():
                ans += i

        if len(ans) == 0:
            return -1

        return ans