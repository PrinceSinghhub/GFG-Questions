# User function Template for python3

class Solution:
    def longestSubstring(self, s, n):

        res, maxi = "", -1
        d = {}
        for i in range(n):
            x = ""
            for j in range(i, n):
                x += s[j]
                if x in s[j + 1:]:
                    if maxi < len(x):
                        maxi = len(x)
                        res = x
                else:
                    break
        return res if res != "" else "-1"
        # code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()

        ob = Solution()
        print(ob.longestSubstring(S, N))
# } Driver Code Ends