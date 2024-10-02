class Solution:
    def countZero(self, N):
        if N < 10:
            return 0

        ans = [1 for i in range(10, N + 1) if "0" in str(i)]
        return len(ans)

ans = Solution()
print(ans.countZero(2000))

