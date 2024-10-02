# User function Template for python3
class Solution:

    # Function to find minimum number of attempts needed in
    # order to find the critical floor.
    def eggDrop(self, n, k):
        dp = []
        for i in range(n + 1):
            temp = [-1] * (k + 1)
            dp.append(temp)

        def solve(n, k):
            if n == 0 or k == 0:
                return 0
            if n == 1:
                return k
            if k == 1:
                return 1

            if dp[n][k] != -1:
                return dp[n][k]

            mn = float("inf")
            for i in range(1, k + 1):
                tmp = max(solve(n - 1, i - 1), solve(n, k - i))
                if tmp < mn:
                    mn = tmp
            dp[n][k] = mn + 1

            return dp[n][k]

        return solve(n, k)


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n, k = map(int, input().strip().split())
        ob = Solution()
        print(ob.eggDrop(n, k))
# } Driver Code Ends