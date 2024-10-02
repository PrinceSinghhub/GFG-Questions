class Solution:
    def maxSubarrayXOR(self, arr, N):
        x = 0
        while True:
            y = max(arr)
            if y == 0:
                return x
            x = max(x, x ^ y)
            arr = [min(z, z ^ y) for z in arr]