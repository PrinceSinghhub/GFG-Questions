class Solution:
    dirList = [[1, 0], [0, -1], [0, 1], [-1, 0]]

    def dfs(self, i, j, idx, mat, target):
        n, m = len(mat), len(mat[0])
        if i >= n or i < 0 or j < 0 or j >= m:
            return 0

        if idx == len(target) - 1:
            return 1 if mat[i][j] == target[idx] else 0

        if mat[i][j] != target[idx]:
            return 0

        result = 0
        temp = mat[i][j]
        mat[i][j] = '#'

        for dx, dy in self.dirList:
            x, y = i + dx, j + dy
            result += self.dfs(x, y, idx + 1, mat, target)

        mat[i][j] = temp

        return result

    def findOccurrence(self, mat, target):

        count = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if target[0] == mat[i][j]:
                    tCount = self.dfs(i, j, 0, mat, target)
                    count += tCount

        return count


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        R = int(line[0])
        C = int(line[1])
        mat = []
        for _ in range(R):
            mat.append([x for x in input().strip().split()])
        target = input()
        obj = Solution()
        print(obj.findOccurrence(mat, target))
# } Driver Code Ends