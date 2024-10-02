class Solution:
    def isDivisibleBy10(self, bin):
        if int(bin, 2) % 10 == 0:
            return 1
        return 0

ans = Solution()
print(ans.isDivisibleBy10("1010"))