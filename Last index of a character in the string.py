class Solution:
    def LastIndex(self, s, p):

        for i in range(len(s) - 1, -1, -1):

            if s[i] == p:
                return i
        return -1


ans = Solution()
S = "Geeks"
P = 'e'
print(ans.LastIndex(S,P))