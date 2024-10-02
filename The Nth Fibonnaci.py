import math


class Solution:
    def fib(self, N):
        first = 0
        second = 1
        third = 0

        for i in range(N):
            third = (first + second) % 10
            second = first
            first = third

        return third

    # {


#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        print(ob.fib(N))