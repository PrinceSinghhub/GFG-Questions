class Solution:
    def MinCoin(self, nums, amount):

        # Code here
        dp = [None for i in range(amount + 1)]
        dp[0] = []
        for i in range(amount + 1):
            if dp[i] is not None:
                for num in nums:
                    combination = [*dp[i], num]
                    if i + num <= amount:
                        if dp[i + num] is None or len(dp[i + num]) > len(combination):
                            dp[i + num] = combination

        if dp[amount] is None:
            return -1
        else:
            return len(dp[amount])

ans = Solution()
arr = [1, 2, 5]
amount = 11
print(ans.MinCoin(arr,amount))