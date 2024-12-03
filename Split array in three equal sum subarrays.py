class Solution:

    def findSplit(self, arr):
        total1 = sum(arr)
        if total1 % 3 != 0:
            return [-1, -1]

        total2, ans = 0, []
        for i in range(len(arr)):
            total2 += arr[i]
            if total2 == total1 // 3:
                total2 = 0
                ans.append(i)
                if len(ans) == 2:
                    return ans

        return [-1, -1]