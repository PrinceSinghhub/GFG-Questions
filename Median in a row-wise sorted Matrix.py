class Solution:
    def median(self, matrix, r, c):
        ans = []
        for i in matrix:
            ans.extend(i)

        ans.sort()

        mid = len(ans) // 2
        return ans[mid]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().strip().split())
        matrix = [[0 for j in range(c)] for i in range(r)]
        line1 = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(r):
            for j in range(c):
                matrix[i][j] = line1[k]
                k += 1
        ans = ob.median(matrix, r, c);
        print(ans)