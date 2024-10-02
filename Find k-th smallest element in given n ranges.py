class Solution:
    def kthSmallestNum(self, n, ranges, q, queries):

        arr = []
        f = ranges[0]
        s = ranges[1]
        for i in range(f[0], f[1] + 1):
            arr.append(i)

        for i in range(s[0], s[1] + 1):
            arr.append(i)

        ans = []
        for qu in queries:
            if qu > len(arr):
                ans.append(-1)
            else:
                ans.append(arr[qu - 1])

        return ans

ans = Solution()
r = [[1,4],[6,8]]
q = [2,6,10]
print(ans.kthSmallestNum(0,r,0,q))