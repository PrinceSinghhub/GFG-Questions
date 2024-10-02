class Solution:

    def sumOfDivisors(self, N):

        s=0

        for i in range(1,N+1):

            s+=(N//i)*i

        return s