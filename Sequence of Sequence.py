class Solution:
    def generate(self, a, m, n):
        total = 0
        lim = m >> n

        while a <= lim:
            if n:
                total += self.generate(a * 2, m, n - 1)
            else:
                total += 1
            a += 1

        return total

    def numberSequence(self, m, n):
        return self.generate(1, m, n - 1)