class Solution:
    def maxLength(self, S):
        lefts = []
        ans = 0
        contin = [False] * len(S)
        for i in range(len(S)):
            if S[i] == "(": lefts.append(i)
            if S[i] == ")" and len(lefts) > 0:
                contin[lefts.pop()] = True
                contin[i] = True
        c = 0
        for i in range(len(S)):
            if not contin[i]:
                ans = max(c, ans)
                c = 0
                continue
            c += 1
        ans = max(c, ans)
        return ans


# {
# Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
# } Driver Code Ends