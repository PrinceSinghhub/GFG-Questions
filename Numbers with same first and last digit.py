class Solution:
    def numbersInRange(self, L, R):

        count = 0
        for i in range(L, R + 1):
            if len(str(i)) == 1:
                count += 1

            else:
                if str(i)[0] == str(i)[-1]:
                    count += 1
        return count

ans = Solution()
print(ans.numbersInRange(11,12))