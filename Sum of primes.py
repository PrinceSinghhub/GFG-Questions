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

    def primeSum(self, N):

        ans = 0

        while N > 0:

            dig = N % 10
            check = self.check(dig)
            if check == True:
                ans += dig
            N = N // 10

        return ans

ans = Solution()
print(ans.primeSum(777))
