# User function Template for python3
import math


class Solution:
    def primarytest(self, N):

        last = int((N ** 0.5))

        for i in range(2, last + 1):

            if N % i == 0:
                return False
        return True

    def hasThreePrimeFac(self, N):

        if N == 1:
            return 0

        check = int((N ** 0.5))

        if int((N ** 0.5)) == (N ** 0.5):

            if self.primarytest(check):
                return 1
        return 0

    # def hasThreePrimeFac(self, N):

    # ans = [i for i in range(1,N+1) if N%i == 0]
    # if len(ans) == 3:
    #     return 1
    # return 0

ans = Solution()
print(ans.hasThreePrimeFac(3528))