class Solution:
    def sequence(self, n):
        if n == 1:
            return 1
        mod = 1000000007
        sums = 0
        temp = 1
        for i in range(n):
            mul = 1
            for j in range(i+1):
                mul= (mul*temp) % mod
                temp +=1
            sums= (sums + mul)%mod
        return sums % mod