# User function Template for python3
mod = 10 ** 9 + 7


class Solution:

    def tras(self, arr, dp, sum, index):
        # Base case
        if index < 0:
            return 1 if sum == 0 else 0

        if dp[index][sum] != -1:
            return dp[index][sum]

        count = 0

        # Include
        if arr[index] <= sum:
            count += self.tras(arr, dp, sum - arr[index], index - 1)

        count += self.tras(arr, dp, sum, index - 1)

        dp[index][sum] = count % mod
        return dp[index][sum]

    def perfectSum(self, arr, n, sum):
        dp = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
        index = n - 1

        return self.tras(arr, dp, sum, index)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, sum = input().split()
        n, sum = int(n), int(sum)
        arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.perfectSum(arr, n, sum)
        print(ans)

# } Driver Code Ends