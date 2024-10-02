from queue import Queue


class Solution:
    def numberOfCells(self, n, m, r, c, u, d, mat):
        visited = [[False for _ in range(m)] for _ in range(n)]

        if mat[r][c] == "#":
            return 0

        visited[r][c] = True
        res = 1
        q = Queue()

        q.put((r, c, u, d))
        while not q.empty():
            y, x, up, down = q.get()

            if x - 1 >= 0 and mat[y][x - 1] == '.' and not visited[y][x - 1]:
                res += 1
                visited[y][x - 1] = True
                q.put((y, x - 1, up, down))

            if x + 1 < m and mat[y][x + 1] == '.' and not visited[y][x + 1]:
                res += 1
                visited[y][x + 1] = True
                q.put((y, x + 1, up, down))

            if y - 1 >= 0 and mat[y - 1][x] == '.' and not visited[y - 1][x] and up > 0:
                res += 1
                visited[y - 1][x] = True
                q.put((y - 1, x, up - 1, down))

            if y + 1 < n and mat[y + 1][x] == '.' and not visited[y + 1][x] and down > 0:
                res += 1
                visited[y + 1][x] = True
                q.put((y + 1, x, up, down - 1))

        return res