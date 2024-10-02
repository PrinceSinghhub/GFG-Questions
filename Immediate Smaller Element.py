class Solution:

    def immediateSmaller(self, arr, n):

        ans = []

        for i in range(n - 1):

            if arr[i] > arr[i + 1]:
                ans.append(arr[i + 1])
            else:
                ans.append(-1)

        ans.append(-1)
        arr[:] = ans

        return arr

ans = Solution()
arr = [5, 6, 2, 3, 1, 7]
print(ans.immediateSmaller(arr,len(arr)-1))