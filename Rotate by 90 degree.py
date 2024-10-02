class Solution:

    # Function to rotate matrix anticlockwise by 90 degrees.
    def rotateby90(self, a, n):

        arr = []

        for i in range(len(a) - 1, -1, -1):
            temp = []
            for j in range(len(a[i])):
                val = a[j][i]
                temp.append(val)
            arr.append(temp)

        a[:] = arr
        return a

ans = Solution()
arr = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
print(ans.rotateby90(arr,3))