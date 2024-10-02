class Solution:
    def movOnGrid(self, r, c):
        r = (r - 1) % 7
        c = (c - 1) % 4
        return ["JON", "ARYA"][r==c]

ans = Solution()
print(ans.movOnGrid(10,12))