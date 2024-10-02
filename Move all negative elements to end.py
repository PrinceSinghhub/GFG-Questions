class Solution:
    def segregateElements(self, arr):
        neg = [i for i in arr if i < 0]
        arr = [i for i in arr if i >= 0]

        return arr + neg

ans =Solution()
arr = [1, -1, 3, 2, -7, -5, 11, 6]
print(ans.segregateElements(arr))