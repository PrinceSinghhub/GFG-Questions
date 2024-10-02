class Solution:

    def check(self, n):

        if n < 2:
            return False

        count = 2

        while count * count <= n:
            if n % count == 0:
                return False
            count += 1

        return True

    def isTwistedPrime(self, N):

        check = self.check(N)
        check1 = self.check(int(str(N)[::-1]))

        if check == True and check1 == True:
            return 1

        return 0

ans = Solution()
print(ans.isTwistedPrime(13))