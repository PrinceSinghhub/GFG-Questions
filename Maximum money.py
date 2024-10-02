class Solution:
    def maximizeMoney(self, N, K):

        # ans = [K for i in range(N) if i%2 == 0]
        # # print(ans)
        # return sum(ans)

        # optimal approch
        if N % 2 == 0:
            return K * (N // 2)
        else:
            mod = N % 2
            div = N // 2
            return K * (mod + div)

ans = Solution()
print(ans.maximizeMoney(101,5))