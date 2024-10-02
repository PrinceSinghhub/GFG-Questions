class Solution:
    def countNumberswith4(self, N):
        arr = [i for i in range(4, N + 1) if str(4) in str(i)]

        if len(arr) == 0:
            return 0

        return len(arr)


ans = Solution()
n = 99
print(ans.countNumberswith4(n))