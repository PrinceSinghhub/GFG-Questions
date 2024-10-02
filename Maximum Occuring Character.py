from collections import Counter


class Solution:

    def getMaxOccurringChar(self, s):
        # code here
        mycounter = Counter(s)

        mycounter = sorted(mycounter.items(), key=lambda x: x[1], reverse=True)

        max = 0
        finaloutput = "z"

        for i in mycounter:
            if i[1] >= max:
                if i[0] <= finaloutput:
                    finaloutput = i[0]
                    max = i[1]
        return finaloutput

ans = Solution()
str = "testsample"
print(ans.getMaxOccurringChar(str))