import math


class Solution:

    def primeCheck(self, x):

        if x == 1:
            return 0

        sta = 1

        for i in range(2, int(math.sqrt(x)) + 1):  # range[2,sqrt(num)]

            if (x % i == 0):
                sta = 0

                break

        return sta

    def NthTerm(self, N):

        i = 0

        while True:

            if self.primeCheck(N - i) == 1 or self.primeCheck(N + i) == 1:
                return i

            i = i + 1