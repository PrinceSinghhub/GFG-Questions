# User function Template for python3

class Solution1(object):
    def climbStairs(self, n):
        mod = 1000000007

        first = 0
        second = 0
        third = 1

        for i in range(n):
            temp1 = second
            temp2 = third

            third = third + second + first
            second = temp2

            first = temp1

        return third % mod


class Solution:
    # Function to count the number of ways in which frog can reach the top.
    def countWays(self, n):
        ans = Solution1()
        return ans.climbStairs(n)

        # code here


# {
#  Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10 ** 6)
# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))
# } Driver Code Ends