# User function Template for python3

class Solution:
    def colName(self, n):
        ch = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        ans = ""

        while n > 25:
            r = n % 26
            if r == 0:
                ans = 'Z' + ans
            else:
                ans = ch[r - 1] + ans
            n = (n - 1) // 26

        r = int(n)
        ans = ch[r - 1] + ans
        return ans


# {
# Driver Code Starts
# Initial Template for Python 3

t = int(input())
for tc in range(t):
    n = int(input())
    ob = Solution()
    print(ob.colName(n))

# } Driver Code Ends