class Solution:
    def segregate0and1(self, arr, n):

        dp = []
        for i in range(n):
            if arr[i] == 1:
                dp.append(1)
            else:
                dp.insert(0, 0)
        arr[:] = dp
        return arr

ans = Solution()
arr = [0, 0, 1, 1, 0]
print(ans.segregate0and1(arr,len(arr)))