class Solution:
    def maxCoins(self, arr, n):
        # Code here
        t = [[0 for i in range(n)] for j in range(n)]
        for g in range(n):
            i = 0
            j = g
            while (j < n):
                if (i + 2 <= j):
                    x = t[i + 2][j]
                else:
                    x = 0
                if (i + 1 <= j - 1):
                    y = t[i + 1][j - 1]
                else:
                    y = 0
                if (i <= j - 2):
                    z = t[i][j - 2]
                else:
                    z = 0
                t[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))
                i += 1
                j += 1
        return t[0][n - 1]


# {
# Driver Code Starts
# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maxCoins(arr, n))
# Contributed By: Harshit Sidhwa
# } Driver Code Ends