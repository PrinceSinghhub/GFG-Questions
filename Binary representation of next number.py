class Solution:
    def binaryNextNumber(self, s):
        val = int(s,2) + 1
        ans = bin(val)[2::]
        return ans