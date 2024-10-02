class Solution:
    def minValue(self, a, b, n):
        a.sort()
        b.sort()

        a = a[::-1]
        Sum = 0
        for i in range(n):
            Sum += a[i] * b[i]

        return Sum

