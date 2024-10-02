class Solution:

    def ans(self, i, n):
        if i>n:
            return
        print(i, end=" ")
        self.ans(i + 1, n)

    def printNos(self, N):
         self.ans(1, N)

ans = Solution()
print(ans.printNos(2))