# User function Template for python3

class Solution:

    # Function to check if a string is Isogram or not.
    def isIsogram(self, s):

        for i in s:
            if s.count(i) == 1:
                continue
            else:
                return False
        return True

ans = Solution()
a = "machine"
print(ans.isIsogram(a))