# User function Template for python3

class Solution:
    def findMinOpeartion(self, matrix, n):

        maxSum = float('-inf')
        for i in range(n):
            sum1 = 0
            sum2 = 0
            for j in range(n):
                sum1 += matrix[i][j]
                sum2 += matrix[j][i]
            maxSum = max(maxSum, max(sum1, sum2))

        ans = 0
        for i in range(n):
            sum_row = 0
            for j in range(n):
                sum_row += matrix[i][j]
            ans += maxSum - sum_row

        return ans


# {
# Driver Code Starts

# Initial Template for Python 3

for _ in range(int(input())):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    ob = Solution()
    print(ob.findMinOpeartion(matrix, n))
# } Driver Code Ends