import math


class Solution:
    def fibSum(self, N):
        f0 = 0
        f1 = 1
        sum1 = 1
        for i in range(N - 1):
            f2 = f0 + f1
            sum1 = (sum1 + f2) % 1000000007
            f0 = f1
            f1 = f2
        return sum1


# {
#  Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.fibSum(N))