from collections import Counter


class Solution:
    def getOddOccurrence(self, arr):

        mydic = Counter(arr)

        for i, j in mydic.items():

            if j % 2 != 0:
                return i
        return -1

ans = Solution()
arr = [1, 2, 3, 2, 3, 1, 3]
print(ans.getOddOccurrence(arr))