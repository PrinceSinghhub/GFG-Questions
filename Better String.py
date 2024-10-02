# {
# Driver Code Starts
# Initial Template for Python 3

# } Driver Code Ends
# User function Template for python3

class Solution:

    def counttheChar(self, s):
        hasMap = {}
        cnt = 1

        for c in s:
            x = 2 * cnt
            if c in hasMap:
                x -= hasMap[c]
            hasMap[c] = cnt
            cnt = x

        return cnt

    def betterString(self, s1, s2):
        return s2 if self.counttheChar(s2) > self.counttheChar(s1) else s1


# {
# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends