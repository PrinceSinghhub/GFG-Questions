class Solution:
    def arraySortedOrNot(self, arr):
        temp = arr.copy()
        temp.sort()

        if arr == temp:
            return 1
        return 0

ans = Solution()
print(ans.arraySortedOrNot([90, 80, 100, 70, 40, 30]))