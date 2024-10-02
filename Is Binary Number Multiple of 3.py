class Solution:
    def isDivisible(self, s):
        if int(s, 2) % 3 == 0:
            return 1

        return 0

ans = Solution()
print(ans.isDivisible("10110"))
a = 60
print(str(a)[0])