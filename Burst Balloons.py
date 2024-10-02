from typing import List


class Solution:
    def maxCoins(self, N: int, arr: List[int]) -> int:
        N += 2
        A = [1] + arr + [1]
        dp = [[0] * (N + 1 - L) for L in range(N + 1)]
        for L in range(3, N + 1):
            for si in range(N - L + 1):
                dp[L][si] = max(A[si] * A[mi] * A[si + L - 1] + dp[mi - si + 1][si] + dp[si + L - mi][mi] for mi in
                                range(si + 1, si + L - 1))
        return dp[N][0]


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
        N = int(input())

        arr = IntArray().Input(N)

        obj = Solution()
        res = obj.maxCoins(N, arr)

        print(res)

# } Driver Code Ends