from collections import Counter


class Solution:

    def maxRepeating(self, arr, n, k):

        arr.sort()

        mydic = Counter(arr)

        Max = max(mydic.values())

        for i in mydic.keys():

            if mydic[i] == Max:
                return i

ans = Solution()
arr = [2, 2, 1, 2]
print(ans.maxRepeating(arr,len(arr)-1,3))