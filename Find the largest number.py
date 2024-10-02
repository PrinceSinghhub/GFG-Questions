class Solution:
    def find(self, N):

        for y in range(N, -1, -1):
            if len(str(y)) == 1:
                return N
            else:
                numStr = list(str(y))
                numStr.sort()
                digit = "".join(numStr)

                if int(digit) == y:
                    return y


ans = Solution()
print(ans.find(200))
