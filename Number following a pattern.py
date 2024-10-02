# User function Template for python3
class Solution:
    def printMinNumberForPattern(self,S):
        ans = ""

        for i in range(len(S) + 1):
            ans += str(1 + i)

        i = 0
        while i < len(S):
            if S[i] == 'D':
                beg = ans[i:]
                while i < len(S) and S[i] == 'D':
                    i += 1
                end = ans[i + 1:]
                ans = ans[:i] + beg[::-1] + end

        return ans


# {
# Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends