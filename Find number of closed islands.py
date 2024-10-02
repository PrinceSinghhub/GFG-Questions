class Solution:
    def dfs(self, x, y, matrix, N, M):
        if x < 0 or y < 0 or x >= N or y >= M or matrix[x][y] == 0:
            return

        matrix[x][y] = 0

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for i in range(4):
            self.dfs(x + dx[i], y + dy[i], matrix, N, M)

    def closedIslands(self, matrix, N, M):
        ans = 0

        for i in range(N):
            for j in range(M):
                if (i == 0 or j == 0 or i == N - 1 or j == M - 1) and matrix[i][j] == 1:
                    self.dfs(i, j, matrix, N, M)

        for i in range(N):
            for j in range(M):
                if matrix[i][j] == 1:
                    self.dfs(i, j, matrix, N, M)
                    ans += 1

        return ans
