class Solution:
    def findClosest(self, arr, n, target):

        arr.sort()

        ans = float('inf')
        coll = 0

        for i in range(n):

            a = abs(arr[i] - target)

            if a <= ans:
                ans = a
                coll = arr[i]
        return coll


ans = Solution()
arr = [1, 3, 6, 7]
k = 4
print(ans.findClosest(arr,len(arr),k))