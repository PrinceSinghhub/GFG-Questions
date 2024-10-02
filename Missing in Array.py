class Solution:
    def missingNumber(self, n, array):
        # code here
        return int((n * (n + 1)) / 2 - sum(array))
