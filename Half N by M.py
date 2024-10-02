class Solution:
    def mthHalf(self, N, M):
        half = N
        ans = []
        for i in range(M):
            ans.append(half)
            half = half // 2

        # print(ans)
        return ans[-1]

ans = Solution()
print(ans.mthHalf(120,3))