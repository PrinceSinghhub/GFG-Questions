class Solution():
    def water_flow(self, mat, p, o):
        n = len(mat)
        m = len(mat[0])
        indian = set()
        arabian = set()

        def dfs(r, c, visit, height):
            if (r, c) in visit or r not in range(n) or c not in range(m) or mat[r][c] < height:
                return
            visit.add((r, c))
            dfs(r - 1, c, visit, mat[r][c])
            dfs(r, c + 1, visit, mat[r][c])
            dfs(r, c - 1, visit, mat[r][c])
            dfs(r + 1, c, visit, mat[r][c])

        for i in range(m):
            dfs(0, i, indian, mat[0][i])
            dfs(n - 1, i, arabian, mat[n - 1][i])
        for i in range(n):
            dfs(i, 0, indian, mat[i][0])
            dfs(i, m - 1, arabian, mat[i][m - 1])
        out = indian.intersection(arabian)
        return len(out)
