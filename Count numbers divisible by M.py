class Solution:
    def countDivisibles(ob, A, B, M):
        ans = [i for i in range(A, B + 1) if i % M == 0]
        return len(ans)

ans = Solution()
print(ans.countDivisibles(12,20,2))