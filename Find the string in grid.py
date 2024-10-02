# User function Template for python3

class Solution:
    def is_valid(self, x, y, n, m, grid, word):
        di = [1, 0, -1, 0, 1, 1, -1, -1]

    dj = [0, 1, 0, -1, 1, -1, 1, -1]

    for t in range(8):
        i, j = x, y
        k = 0

        while 0 <= i < n and 0 <= j < m and k < len(word) and grid[i][j] == word[k]:
            i += di[t]
            j += dj[t]
            k += 1

        if k == len(word):
            return True

    return False


def searchWord(self, grid, word):
    n = len(grid)
    m = len(grid[0])

    ans = []

    for i in range(n):
        for j in range(m):
            if grid[i][j] == word[0] and self.is_valid(i, j, n, m, grid, word):
                ans.append([i, j])

    return ans


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n);
        m = int(m);
        grid = []
        for _ in range(n):
            cur = input()
            temp = []
            for __ in cur:
                temp.append(__)
            grid.append(temp)
        word = input()
        obj = Solution()
        ans = obj.searchWord(grid, word)
        for _ in ans:
            for __ in _:
                print(__, end=" ")
            print()
        if len(ans) == 0:
            print(-1)

# } Driver Code Ends