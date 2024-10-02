class Solution:
    def printLargest(self, n, arr):
        arr.sort(key=lambda x: int(x + arr[0]) - int(arr[0] + x), reverse=True)
        return ''.join(arr)


