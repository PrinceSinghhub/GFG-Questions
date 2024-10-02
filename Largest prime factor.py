# User function Template for python3
import math


class Solution:

    def largestPrimeFactor(self, n):
        maxPrime = -1

        # Print the number of 2s that divide n
        while n % 2 == 0:
            maxPrime = 2
            n >>= 1  # equivalent to n /= 2

        # n must be odd at this point
        while n % 3 == 0:
            maxPrime = 3
            n = n / 3

            # now we have to iterate only for integers
        # who does not have prime factor 2 and 3
        for i in range(5, int(math.sqrt(n)) + 1, 6):
            while n % i == 0:
                maxPrime = i
                n = n / i
            while n % (i + 2) == 0:
                maxPrime = i + 2
                n = n / (i + 2)

        # This condition is to handle the
        # case when n is a prime number
        # greater than 4
        if n > 4:
            maxPrime = n

        return int(maxPrime)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.largestPrimeFactor(N))