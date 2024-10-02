# User function Template for python3
class Solution:
    def commonSubseq(ob, S1, S2):
        res = 0
        for i in S1:
            if i in S2:
                res += 1
                break
        return res
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1, S2 = input().split()

        ob = Solution()
        print(ob.commonSubseq(S1, S2))
