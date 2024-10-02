class Solution:
    def areRotations(self,s1, s2):
        s1 = s1 + s1
        return s2 in s1