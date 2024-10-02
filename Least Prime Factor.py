class Solution:

    def leastPrimeFactor(self, n):
        # code here
        flag = [False for _ in range(n + 1)]
        sprime = [0 for _ in range(n + 1)]

        flag[0] = flag[1] = True
        sprime[0], sprime[1] = 0, 1

        for i in range(2, n + 1):
            x = i
            while x < n + 1:

                if not flag[x]:
                    flag[x] = True
                    sprime[x] = i

                x += i

        return sprime