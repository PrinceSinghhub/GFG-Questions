# User function Template for python3

class Solution:
    def printSpiral(self, mat):
        # Define ans array to store the result.
        ans = []

        n = len(mat)  # no. of rows
        m = len(mat[0])  # no. of columns

        # Initialize the pointers reqd for traversal.
        top = 0
        left = 0
        bottom = n - 1
        right = m - 1

        # Loop until all elements are not traversed.
        while (top <= bottom and left <= right):
            # For moving left to right
            for i in range(left, right + 1):
                ans.append(mat[top][i])

            top += 1

            # For moving top to bottom.
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])

            right -= 1

            # For moving right to left.
            if (top <= bottom):
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])

                bottom -= 1

            # For moving bottom to top.
            if (left <= right):
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])

                left += 1

        return ans

    def findK(self, a, n, m, k):

        arr = self.printSpiral(a)
        # print(arr)
        return arr[k - 1]

        # Write Your Code here


# {
# Driver Code Starts

# Initial Template for Python 3

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = [
        list(map(int, input().split()))
        for _ in range(n)
    ]

    ob = Solution()
    print(ob.findK(a, n, m, k))

# } Driver Code Ends