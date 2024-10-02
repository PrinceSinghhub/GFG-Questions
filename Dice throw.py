class Solution:
    def throw_dice(self, M, N, X):
        if N == 0 and X == 0:
            return 1
        if N == 0 and X > 0:
            return 0
        cnt = 0
        for i in range(1, M + 1):
            if X >= i:
                cnt += self.throw_dice(M, N - 1, X - i)
        return cnt

    def noOfWays(self, M, N, X):
        return self.throw_dice(M, N, X)


class Solution:
    def throw_dice(self, M, N, X, mem):
        if N == 0 and X == 0:
            mem[N][X] = 1
            return mem[N][X]
        if N == 0 and X > 0:
            mem[N][X] = 0
            return mem[N][X]
        if mem[N][X] != -1:
            return mem[N][X]
        cnt = 0
        for i in range(1, M + 1):
            if X >= i:
                cnt += self.throw_dice(M, N - 1, X - i, mem)
        mem[N][X] = cnt
        return mem[N][X]

    def noOfWays(self, M, N, X):
        mem = [[-1] * (X + 1) for i in range(N + 1)]
        return self.throw_dice(M, N, X, mem)


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        M, N, X = map(int, input().split())

        ob = Solution()
        print(ob.noOfWays(M, N, X))