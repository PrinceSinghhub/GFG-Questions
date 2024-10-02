class Solution:
    def posIntSol(self, s):
        def calnCr(n, r):
            f = [1 for i in range(n + 1)]
            for i in range(1, n + 1):
                f[i] = f[i - 1] * i
            return f[n] // (f[r] * f[n - r]);

        cnt = 0
        idx = 0
        for i in range(len(s)):
            cnt += (s[i] == '+')
            if s[i] == '=':
                idx = i
        n = cnt + 1
        k = int(s[idx + 1:])
        if (n > k):
            return 0
        n = n - 1
        k = k - 1
        return calnCr(k, n)