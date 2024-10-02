from typing import List


class Solution:
    def primeFactorizationSieve(self, b):
        prime_factors = [0] * (b + 1)

        for i in range(2, int(b ** 0.5) + 1):
            if prime_factors[i] == 0:
                for j in range(i * i, b + 1, i):
                    if prime_factors[j] == 0:
                        prime_factors[j] = i

        for i in range(2, b + 1):
            if prime_factors[i] == 0:
                prime_factors[i] = i

        return prime_factors

    def sumOfPowers(self, a: int, b: int) -> int:

        prime_factors = self.primeFactorizationSieve(b)

        result = 0
        for num in range(a, b + 1):
            temp = num
            power_sum = 0
            while temp > 1:
                prime = prime_factors[temp]
                count = 0
                while temp % prime == 0:
                    temp //= prime
                    count += 1
                power_sum += count

            result += power_sum

        return result


# {
# Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  # array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a = int(input())
        b = int(input())

        obj = Solution()
        res = obj.sumOfPowers(a, b)

        print(res)

# } Driver Code Ends