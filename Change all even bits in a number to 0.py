class Solution:
    def convertEvenBitToZero(self,n):
        # hexa decimal value  0xaaaaaaaa
        return (n & 0xaaaaaaaa)


ans = Solution()
print(ans.convertEvenBitToZero(5))


