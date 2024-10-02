class Solution:

    def countPaths(self, N):

        if N == 1:
            return 0

        mod = 10 ** 9 + 7

        t1 = 1

        t2 = 0

        for i in range(2, N):
            t2, t1 = t1, (2 * t1 + 3 * t2) % mod

        ans = (3 * t1) % mod

        return ans