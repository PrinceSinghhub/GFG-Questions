class Solution:

    # Function to remove common characters and concatenate two strings.
    def concatenatedString(self, s1, s2):

        temp = s1 + s2
        ans = ""

        for i in temp:
            if i in s1 and i in s2:
                continue
            else:
                ans += i

        if len(ans) == 0:
            return -1
        return ans
ans = Solution()
s1 = 'aacdb'
s2 = 'gafd'
print(ans.concatenatedString(s1,s2))
