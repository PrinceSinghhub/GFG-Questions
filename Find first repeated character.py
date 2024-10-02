# User function Template for python3

class Solution:

    def firstRepChar(self, s):
        dict = {}

        for i in s:
            if i in dict:

                return i
            else:
                dict[i] = 1
        return -1

ans = Solution()
S="geeksforgeeks"
print(ans.firstRepChar(S))