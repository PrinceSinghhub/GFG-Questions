import sys


class Solution:
    def __init__(self):
        self.char = 'A'
        self.cnt = 0
        self.string = ""

    def showBrackets(self, i, j, brackets):
        if i == j:
            if self.cnt != 0:
                self.string += (ord(self.char) + self.cnt)
            else:
                self.string += self.char

            if self.char == 'Z':
                self.char = 'A'
                self.cnt += 1
            else:
                self.char = chr(ord(self.char) + 1)
        else:
            self.string += "("
            self.showBrackets(i, brackets[i][j], brackets)
            self.showBrackets(brackets[i][j] + 1, j, brackets)
            self.string += ")"

        return self.string

    def matrixChainOrder(self, p, n):
        # code here
        n -= 1
        ans = [[0] * (n) for i in range(n)]
        brackets = [[0] * (n) for i in range(n)]
        size, j = 1, 0
        cost = 0

        while size < n:
            i = 0
            while i < (n - size):
                j = i + size
                ans[i][j] = sys.maxsize
                k = i
                while k < j:
                    cost = ans[i][k] + ans[k + 1][j] + p[i] * p[j + 1] * p[k + 1]
                    if cost < ans[i][j]:
                        ans[i][j] = cost
                        brackets[i][j] = k

                    k += 1

                i += 1

            size += 1

        return self.showBrackets(0, n - 1, brackets)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = input().split()
        for i in range(n):
            p[i] = int(p[i])

        ob = Solution()
        print(ob.matrixChainOrder(p, n))
# } Driver Code Ends