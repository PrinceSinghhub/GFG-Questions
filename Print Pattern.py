class Solution:
    def pattern(self, N):
        m = N
        l = []

        while m > 0:
            l.append(m)
            m = m - 5

        while m <= N:
            l.append(m)
            m = m + 5

        return l