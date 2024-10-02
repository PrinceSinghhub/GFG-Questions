class Solution:
    def rearrange(self, arr, n):

        neg = []
        pos = []

        for i in arr:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)

        arr.clear()
        arr[:] = pos[:]
        index = 1

        for i in range(len(neg)):
            arr.insert(index, neg[i])
            index += 2

        return arr


ans = Solution()
arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
print(ans.rearrange(arr,7))