class Solution:
    def findGCD(self, a, b):

        if a == 0:
            return b

        return self.findGCD(b % a, a)

    def gcd(self, n, arr):

        if n < 2:
            return arr[0]

        gcd = self.findGCD(arr[0], arr[1])

        for i in range(2, n):
            gcd = self.findGCD(gcd, arr[i])

        return gcd

ans = Solution()
arr = [2, 4, 6]
n = 3
print(ans.gcd(n,arr))

for i in range(0,10,2):
    print(i)