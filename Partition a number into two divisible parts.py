class Solution:
    def stringPartition(ob, S, a, b):

        ans = ""

        i = 1

        while i < len(S):

            first = S[0:i]
            last = S[i:]

            if int(first) % a == 0 and int(last) % b == 0:
                ans = first + " " + last
                break
            i += 1

        if len(ans) == 0:
            return -1

        return ans

ans = Solution()

s = "1200"
a = 2
b = 4
print(ans.stringPartition(s,a,b))
