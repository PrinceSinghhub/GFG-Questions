class Solution:
    def removeDups(self, S):
        out = ''
        for i in S:
            if i in out:
                pass
            else:
                out+=i
        return out
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)