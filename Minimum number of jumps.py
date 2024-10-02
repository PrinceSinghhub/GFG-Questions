class Solution:
    def minJumps(self, arr, l, n):

        if (n == l):
            return 0

        if (arr[l] == 0):
            return float('inf')

        min = float('inf')
        for i in range(l + 1, n + 1):
            if (i < l + arr[l] + 1):
                jumps = self.minJumps(arr, i, n)
                if (jumps != float('inf') and
                        jumps + 1 < min):
                    min = jumps + 1

        return min

ans = Solution()
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(ans.minJumps(arr,0,len(arr)))