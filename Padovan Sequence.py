class Solution:
    def padovanSequence(self, n):
        if n <= 2:
            return 1
        pprev, prev, curr = 1, 1, 1
        for _ in range(3, n + 1):
            pprev, prev, curr = prev, curr, (prev + pprev) % (10 ** 9 + 7)
        return curr
