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

    def fullPrime(self, N):

        ans = self.check(N)
        if ans == True:
            con = str(N)
            for i in con:
                temp = self.check(int(i))
                if temp == True:
                    continue
                else:
                    return 0

            return 1
        else:
            return 0

ans = Solution()
print(ans.fullPrime(30))
