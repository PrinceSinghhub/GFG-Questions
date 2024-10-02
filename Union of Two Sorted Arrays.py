class Solution:
    def findUnion(self, arr1, arr2, n, m):
        arr1.extend(arr2)
        a = list(set(arr1))
        a.sort()
        return a