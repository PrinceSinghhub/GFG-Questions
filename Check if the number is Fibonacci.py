import math


class Solution:

    def isSquare(self, n):

        s = int(math.sqrt(n))

        return n == s * s

    def checkFibonacci(self, n):

        if self.isSquare(5 * n * n + 4) == True or self.isSquare(5 * n * n - 4) == True:
            return "Yes"

        else:
            return 'No'