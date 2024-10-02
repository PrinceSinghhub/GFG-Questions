class Solution:

    def rotateMatrix(self, arr, n):
        for i in range(n):
            for j in range(1 + i, n):
                arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
        for k in range(n // 2):
            for l in range(n):
                arr[k][l], arr[n - 1 - k][l] = arr[n - 1 - k][l], arr[k][l]
        return arr

    # def rotateMatrix(self,arr, n):
    #     # code here

    #     ans = []

    #     for i in range(n-1,-1,-1):

    #         temp = []

    #         for j in range(n):

    #             temp.append(arr[j][i])

    #         ans.append(temp)

    #     return ans


# {
#  Driver Code Starts
# Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        inputLine = list(map(int, input().strip().split()))
        arr = [[0 for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                arr[i][j] = inputLine[i * n + j]
        ob = Solution()
        ob.rotateMatrix(arr, n)
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=" ")
        print()
        tc -= 1
