from typing import List

class Solution:
    def isvalid(self, n, m, x, y):
        if x >= n or x < 0:
            return False
        if y >= m or y < 0:
            return False
        return True

    def shortestDistance(self, n: int, m: int, g: List[List[int]], x: int, y: int) -> int:
        movements = [(1, 0), (0, -1), (0, 1), (-1, 0)]
        vis = [[False for _ in range(m)] for _ in range(n)]
        lev = [[-1 for _ in range(m)] for _ in range(n)]
        q = [(0, 0)]
        lev[0][0] = 0
        vis[0][0] = True

        while q:
            vx, vy = q.pop(0)
            if vx == x and vy == y:
                return lev[x][y]

            for movement in movements:
                child_x = vx + movement[0]
                child_y = vy + movement[1]
                if self.isvalid(n, m, child_x, child_y) and g[child_x][child_y] and not vis[child_x][child_y]:
                    lev[child_x][child_y] = lev[vx][vy] + 1
                    vis[child_x][child_y] = True
                    q.append((child_x, child_y))

        return -1
