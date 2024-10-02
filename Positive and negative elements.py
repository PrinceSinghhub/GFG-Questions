class Solution:
    def arranged(self, a):

        pos = []
        neg = []

        for i in a:
            if i > 0:
                pos.append(i)
            else:
                neg.append(i)

        ans = []
        ind = 0
        for i in pos:
            ans.append(i)
            if ind < len(neg):
                ans.append(neg[ind])
                ind += 1
        return ans

ans = Solution()
arr = [-1, 2, -3, 4, -5, 6]
print(ans.arranged(arr))