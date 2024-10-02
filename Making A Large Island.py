from typing import List


class disjoint:
    def __init__(self, n):
        self.par = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    def findp(self, n):
        if n == self.par[n]:
            return n
        self.par[n] = self.findp(self.par[n])
        return self.par[n]

    def unionn(self, u, v):
        uu, uv = self.findp(u), self.findp(v)
        if uu == uv:
            return
        if self.size[uu] < self.size[uv]:
            self.par[uu] = uv
            self.size[uv] += self.size[uu]
        else:
            self.par[uv] = uu
            self.size[uu] += self.size[uv]


def maximumIslandSize(grid):
    n = len(grid)
    ds = disjoint(n * n)

    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                continue

            drow, dcol = [-1, 0, 1, 0], [0, -1, 0, 1]
            for k in range(4):
                nr, nc = r + drow[k], c + dcol[k]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
                    node = r * n + c
                    newn = nr * n + nc
                    ds.unionn(node, newn)

    maxx = 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                continue

            drow, dcol = [-1, 0, 1, 0], [0, -1, 0, 1]
            component = set()
            for k in range(4):
                nr, nc = r + drow[k], c + dcol[k]
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
                    newn = nr * n + nc
                    component.add(ds.findp(newn))

            total = sum(ds.size[i] for i in component)
            maxx = max(maxx, total + 1)

    for cell in range(n * n):
        maxx = max(maxx, ds.size[ds.findp(cell)])
    return maxx


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        return maximumIslandSize(grid)


# {
# Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        # matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())

        grid = IntMatrix().Input(n, n)

        obj = Solution()
        res = obj.largestIsland(grid)

        print(res)
# } Driver Code Ends