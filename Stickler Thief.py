# User function Template for python3

class Solution:

    # Function to find the maximum money the thief can get.
    def FindMaxSum(houses, n):
        if n == 0:
            return 0

        prev_max = 0
        curr_max = 0

        for i in range(n):
            max_amount = max(curr_max, prev_max + houses[i])
            prev_max = curr_max
            curr_max = max_amount

        return curr_max2


# {
# Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10 ** 6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.FindMaxSum(a, n))
# } Driver Code Ends