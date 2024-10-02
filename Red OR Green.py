class Solution:
    def RedOrGreen(self, N, S):
        r = 0
        g = 0
        for i in S:
            if i == 'R':
                r+=1
            if i == 'G':
                g+=1
        res = min(r,g)
        return res



if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        S = input()
        ob = Solution()
        print(ob.RedOrGreen(N, S))