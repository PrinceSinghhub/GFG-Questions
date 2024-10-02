class Solution:
    def posOfRightMostDiffBit(self,m,n):
        if m==n:
            return -1
        m^=n
        for i,v in enumerate(bin(m)[2:][::-1]):
            if v=='1':
                return i+1