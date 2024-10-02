import math


class Solution:
    def nthFibonacci(self, n):


         # using formula
         # divid = math.sqrt(5)
         # ans = math.pow(((1+math.sqrt(5))/2),n)
         # return round(ans/divid)

         a, b = 0, 1
         if n == 1:
             return 0
         if n == 2:
             return 1
         for i in range(n - 2):
             b = a + b
             a = b - a
         return (a + b) % 1000000007








# {
#  Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(10 ** 6)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.nthFibonacci(n))