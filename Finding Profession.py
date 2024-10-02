class Solution:
    def profession(self, level, pos):

        count = 0
        n = pos - 1

        while n:
            n &= n - 1
            count += 1

        if count & 1:
            return 'd'
        else:
            return 'e'

ans = Solution()

level = 4
pos = 2
print(ans.profession(level,pos))