class Solution:
    def solveQueries(self, n, Queries):

        ans = [[0] * n for _ in range(n)]
        for [up, left, down, right] in Queries:
            ans[up][left] += 1
            if right + 1 < n:
                ans[up][right + 1] -= 1
            if down + 1 < n:
                ans[down + 1][left] -= 1
                if right + 1 < n:
                    ans[down + 1][right + 1] += 1
        for i in range(n - 1):
            for j in range(n):
                ans[i + 1][j] += ans[i][j]
        for i in range(n):
            for j in range(1, n):
                ans[i][j] += ans[i][j - 1]
        return ans