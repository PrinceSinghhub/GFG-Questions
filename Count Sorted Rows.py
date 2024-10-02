class Solution:
    def sortedCount(self,Mat):

        count = 0

        for i in Mat:
            temp = i.copy()

            i.sort()

            if i == temp or temp == i[::-1]:
                count += 1
        return count

ans = Solution()
mat = [[1,2,3],
       [6,5,4],
       [7,9,8]]
print(ans.sortedCount(mat))