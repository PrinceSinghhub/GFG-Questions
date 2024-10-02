class Solution:
    def firstRep(self, s):

        for i in s:
            if s.count(i) > 1:
                return i
        return -1

ans = Solution()
S = "geeksforgeeks"
print(ans.firstRep(S))