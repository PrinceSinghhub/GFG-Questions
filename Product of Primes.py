class Solution:
    def findPrime(self, n):

        count = 2

        while (count * count) <= n:

            if n % count == 0:
                return False

            count += 1

        return True

    def primeProduct(self, L, R):

        ans = 1
        mod = 1000000007
        for i in range(L, R + 1):
            if i >= 2:
                res = self.findPrime(i)
                if res == True:
                    ans = ans * i
                    ans = ans % mod

        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, R = [int(x) for x in input().split()]

        ob = Solution()
        print(ob.primeProduct(L, R))