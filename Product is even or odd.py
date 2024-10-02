class Solution:
    def EvenOdd(self, n1, n2):
        if (int(n1) * int(n2)) % 2 == 0:
            return 1
        return 0

ans = Solution()
n = "20"
a = "60"
print(ans.EvenOdd(n,a))