class Solution:
    def longestCommonSubstring(self, string1, string2):
        max_length = 0
        n = len(string1)

        for start in range(n):
            for end in range(start, n):
                substring = string1[start:end + 1]
                if substring in string2:
                    max_length = max(max_length, len(substring))

        return max_length
