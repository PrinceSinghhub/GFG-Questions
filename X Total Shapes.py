seen = set()


def dfs(i, j, n, m, grid):
    global seen
    if i < 0 or i >= m or j < 0 or j >= n: return
    if (i, j) in seen: return
    seen.add((i, j))
    if grid[i][j] == "X":
        dfs(i + 1, j, n, m, grid)
        dfs(i - 1, j, n, m, grid)
        dfs(i, j + 1, n, m, grid)
        dfs(i, j - 1, n, m, grid)


class Solution:

    def xShape(self, grid):
        global seen

        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(0, m):
            for j in range(0, n):
                if (i, j) not in seen and grid[i][j] == "X":
                    dfs(i, j, n, m, grid)
                    count += 1

        seen.clear()
        return count


# {
# Driver Code Starts


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = map(int, input().split())
        grid = [['#' for i in range(m)] for j in range(n)]
        for i in range(n):
            s = input().strip()
            for j in range(m):
                grid[i][j] = s[j]
        obj = Solution()
        ans = obj.xShape(grid)
        print(ans)
# } Driver Code Ends