class Solution:
    def divisibleBy5(ob, N):
        if int(N) % 5 == 0:
            return 1
        return 0

ans = Solution()
print(ans.divisibleBy5("50"))