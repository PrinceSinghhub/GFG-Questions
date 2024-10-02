class Solution:
    def numberWithNoConsecutiveOnes(self, n):
        # Code here
        kk = []
        kk.append("1")
        k = 2 ** n - 1
        for i in range(2, k):
            m = bin(i)
            mm = str(m)

            if '11' not in mm:
                kk.append(i)

        return kk