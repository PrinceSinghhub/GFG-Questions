class Solution:
    def kthDigit(self, A, B, K):
        ans = str(A ** B)
        return int(ans[-K])

ans = Solution()
print(ans.kthDigit(10,3,3))