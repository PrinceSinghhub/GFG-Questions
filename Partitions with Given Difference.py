from typing import List


class Solution:
    def countPartitions(self, n: int, d: int, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        total_sum = sum(arr)

        # Check if sum(arr) + d is even
        if (total_sum + d) % 2 != 0:
            return 0

        # Calculate the target sum for one subset
        target_sum = (total_sum + d) // 2

        # Edge case: If target_sum is negative, it's not possible
        if target_sum < 0:
            return 0

        # Initialize the dp array
        dp = [0] * (target_sum + 1)
        dp[0] = 1  # There is one way to make the sum 0 (using no elements)

        # Update dp array for each number in arr
        for num in arr:
            for j in range(target_sum, num - 1, -1):
                dp[j] = (dp[j] + dp[j - num]) % MOD

        return dp[target_sum]


# {
# Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        d = int(input())

        arr = IntArray().Input(n)

        obj = Solution()
        res = obj.countPartitions(n, d, arr)

        print(res)

# } Driver Code Ends