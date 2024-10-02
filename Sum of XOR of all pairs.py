class Solution:
    def sumXOR (self, a, n):
        sum1 = 0
        for i in range(0,32):
            nzero = 0
            none = 0
            for j in a:
                if (j & (1 << i)):
                    nzero += 1
                else:
                    none += 1
            sum1 = sum1 + (nzero * none) * (1 << i)
        return sum1
