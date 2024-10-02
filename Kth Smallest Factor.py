class Solution:
    def kThSmallestFactor(self, N, K):
        # code here

        ans = []

        for i in range(1, N + 1):
            if N % i == 0:
                ans.append(i)

        if K > len(ans):
            return -1
        else:
            return ans[K - 1]


# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N, K = map(int, input().split())

        ob = Solution()
        print(ob.kThSmallestFactor(N, K))
# } Driver Code Ends