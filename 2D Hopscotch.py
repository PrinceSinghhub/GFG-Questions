class Solution:

    def valid(self, i, j, n, m):

        if i >= 0 and j >= 0 and i < n and j < m:
            return True

        return False

    def hopscotch(self, n, m, mat, ty, i, j):

        # code here

        if ty == 0:

            sums = 0

            if j % 2 == 0:

                arr = [[-1, 0], [-1, 1], [0, 1], [1, 0], [0, -1], [-1, -1]]

                for x in arr:

                    i1 = i + x[0]

                    j1 = j + x[1]

                    if self.valid(i1, j1, n, m): sums += mat[i1][j1]

            else:

                arr = [[-1, 0], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]

                for x in arr:

                    i1 = i + x[0]

                    j1 = j + x[1]

                    if self.valid(i1, j1, n, m): sums += mat[i1][j1]

        else:

            sums = 0

            if j % 2 == 0:

                arr = [[-2, -1], [-2, 0], [-2, 1], [-1, 2], [0, 2], [1, 2], [1, 1], [2, 0], [1, -1], [1, -2], [0, -2],
                       [-1, -2]]

                for x in arr:

                    i1 = i + x[0]

                    j1 = j + x[1]

                    if self.valid(i1, j1, n, m): sums += mat[i1][j1]

            else:

                arr = [[-1, -2], [-1, -1], [-2, 0], [-1, 1], [-1, 2], [0, 2], [1, 2], [2, 1], [2, 0], [2, -1], [1, -2],
                       [0, -2]]

                for x in arr:

                    i1 = i + x[0]

                    j1 = j + x[1]

                    if self.valid(i1, j1, n, m): sums += mat[i1][j1]

        return sums


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = [[0] * m for x in range(n)]
        for i in range(n):
            arr = input().split()
            for j in range(m):
                mat[i][j] = int(arr[j])
        ty, i, j = map(int, input().strip().split())

        ob = Solution()
        print(ob.hopscotch(n, m, mat, ty, i, j))
# } Driver Code Ends