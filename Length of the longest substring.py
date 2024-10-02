class Solution:
    def longestUniqueSubsttr(self, S):
        h = {}  # dict to maintain distinct element count
        res = 1
        i = 0
        while i < len(S):
            if S[i] in h:  # if any char is repeating
                res = max(res, len(h))  # clear current dict
                i = h[S[i]] + 1  # start from where broke
                h.clear()

            else:
                h[S[i]] = i
                i += 1
        res = max(res, len(h))  # if all are distinct
        return res


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()

        ob = Solution()
        print(ob.longestUniqueSubsttr(s))