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

    def singleDigit(self, N):

        temp = 0
        for i in str(N):
            temp += int(i)

        if temp > 9:
            print(temp)
            return self.singleDigit(temp)
        print(temp)
        return temp

    def digitsPrime(self, N):

        digit = self.singleDigit(N)

        check = self.check(digit)
        if check == True:
            return 1

        return 0

ans = Solution()
print(ans.digitsPrime(12))