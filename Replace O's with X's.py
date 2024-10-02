# User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here

        rows, cols = len(mat), len(mat[0])

        def capture(r, c):
            if r < 0 or c < 0 or r == rows or c == cols or mat[r][c] != "O":
                return
            mat[r][c] = "T"
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Capture unsurrounded regions(O -> T)
        for r in range(rows):
            for c in range(cols):
                if (mat[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1])):
                    capture(r, c)

        # Capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == "O":
                    mat[r][c] = "X"

        # Unapture unsurrounded regions (T -> O)
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == "T":
                    mat[r][c] = "O"

        return mat


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str, input().split()))
            mat.append(s)

        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()
# } Driver Code Ends