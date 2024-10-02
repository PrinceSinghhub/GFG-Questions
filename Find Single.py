class Solution:
    def findSingle(self, arr):
        ans = 0

        for i in arr:
            ans = ans ^ i

        return ans

        # copy = arr.copy()

        # for i in copy:
        #     if copy.count(i) > 1:
        #         arr.remove(i)

        # return arr[0]




ans = Solution()
arr = [1, 2, 3, 5, 3, 2, 1, 4, 5, 6, 6]
print(ans.findSingle(arr))

