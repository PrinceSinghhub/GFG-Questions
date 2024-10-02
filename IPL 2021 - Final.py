class Solution:
    def findMaxLen(ob, S):
        n = len(S)
        o, c, a = 0, 0, 0
        for i in range(n):
            if (S[i] == '('):
                o += 1
            else:
                c += 1
            if (o == c):
                a = max(a, o + c)
            if (c > o):
                o, c = 0, 0
        o, c = 0, 0
        i = n - 1
        while (i >= 0):
            if (S[i] == '('):
                o += 1
            else:
                c += 1
            if (o == c):
                a = max(a, o + c)
            if (o > c):
                o, c = 0, 0
            i -= 1
        return a


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.findMaxLen(S))