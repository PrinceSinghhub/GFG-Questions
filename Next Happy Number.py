class Solution:
    def nextHappy(self, n):

        def isHappy(n):
            seen = set()
            while n not in seen:
                seen.add(n)
                n = sum([int(x) ** 2 for x in str(n)])
            return n == 1

        n += 1
        while not isHappy(n):
            n += 1

        return n