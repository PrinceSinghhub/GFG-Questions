class Solution:

    # Function to search a given number in row-column sorted matrix.
    def search(self, matrix, n, m, x):

        for i in matrix:
            if x in i:
                return 1

        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        size = input().strip().split()
        r = int(size[0])
        c = int(size[1])
        line = input().strip().split()
        matrix = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                matrix[i][j] = int(line[i * c + j])
        target = int(input())
        obj = Solution()
        if (obj.search(matrix, r, c, target)):
            print(1)
        else:
            print(0) 