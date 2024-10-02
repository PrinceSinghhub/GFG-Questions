# User function Template for python3im
from math import sqrt


class Solution:
    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    def is_digit_prime(self, n):
        for i in str(n):
            if not self.is_prime(int(i)):
                return False
        return True

    # Function to find nth number made of only prime digits.
    def nthprimedigitsnumber(self, n):
        # code here
        c = 0
        i = 2
        while True:
            if self.is_digit_prime(i):

                c += 1
                if c == n:
                    break
            i += 1
        return i