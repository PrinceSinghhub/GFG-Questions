class Solution:
    def isPerfectNumber(self, N):

        ans = []
        for i in range(1, N):
            if N % i == 0:
                ans.append(i)

        if sum(ans) == N:
            return 1

        return 0


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.isPerfectNumber(N))