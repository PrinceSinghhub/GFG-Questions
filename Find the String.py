#User function Template for python3

class Solution:
    def __init__(self):
        self.K = 0
        self.N = 0
        self.tot = 0
        self.st = set()
        self.ans = ""

    def dfs(self):
        if len(self.st) == self.tot:
            return True

        tmp = ""
        if self.N > 1:
            tmp = self.ans[-self.N + 1:]

        for i in range(self.K):
            tmp += str(i)
            if tmp not in self.st:
                self.ans += str(i)
                self.st.add(tmp)
                if self.dfs():
                    return True
                self.st.remove(tmp)
                self.ans = self.ans[:-1]
            tmp = tmp[:-1]

        return False

    def findString(self, n, k):
        self.K = k
        self.N = n
        self.st.clear()

        if n == 1:
            return "".join(str(i) for i in range(k))

        self.tot = 1
        for i in range(1, n + 1):
            self.tot *= k

        ansa = ['0'] * n
        self.ans = "".join(ansa)
        self.st.add(self.ans)
        self.dfs()

        return self.ans





#{
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())

        ob = Solution()
        ans = ob.findString(N,K)
        ok = 1
        for i in ans:
            if ord(i)<48 or ord(i)>K-1+48:
                ok = 0
        if not ok:
            print(-1)
            continue
        d = dict()
        i = 0
        while i+N-1<len(ans):
            d[ans[i:i+N]] = 1
            i += 1
        tot = pow(K,N)
        if len(d)==tot:
            print(len(ans))
        else:
            print(-1)
# } Driver Code Ends