class Solution:
    def removeConsonants(self, s):
        # complete the function here

        v = 'aeiou'

        ans = ""
        for i in s:
            if i.lower() in v:
                ans += i
        if len(ans) == 0:
            return "No Vowel"
        return ans


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        print(ob.removeConsonants(s))