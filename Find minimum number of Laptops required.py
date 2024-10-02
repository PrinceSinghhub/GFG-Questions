from collections import defaultdict


class Solution:
    def minLaptops(self, N, start, end):
        discrete = defaultdict(int)
        for s, e in zip(start, end):
            discrete[s] += 1
            discrete[e] -= 1

        cur, res = 0, 0
        for t in sorted(discrete):
            cur += discrete[t]
            res = max(res, cur)

        return res


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        N = int(input())
        start = list(map(int, input().split()))
        end = list(map(int, input().split()))

        ob = Solution()
        print(ob.minLaptops(N, start, end))

        T -= 1

# } Driver Code Ends