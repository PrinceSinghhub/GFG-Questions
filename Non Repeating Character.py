# vvvv imp questoion
class Solution:

    def nonrepeatingCharacter(self, s):

        arr = []
        chardic = {}
        for c in s:
            if c in chardic:
                chardic[c] += 1
            else:
                chardic[c] = 1
                arr.append(c)
        for c in arr:
            if chardic[c] == 1:
                return c
        return -1



if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonrepeatingCharacter(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)